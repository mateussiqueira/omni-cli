"""Memory optimization commands for Omni CLI."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

import psutil
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from omni.core.config import config
from omni.core.executor import run_command

app = typer.Typer(help="Mac memory optimization using Thunderbolt 4 SSD")
console = Console()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Memory management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Memory[/bold blue] - Use [cyan]omni memory --help[/cyan]"))


@app.command("status")
def status() -> None:
    """Show current memory and swap status."""
    table = Table(title="🧠 Mac Memory Status", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_usage("/")

    table.add_row("Total RAM", f"{mem.total / (1024**3):.2f} GB")
    table.add_row("Available RAM", f"{mem.available / (1024**3):.2f} GB")
    table.add_row("Used RAM", f"{mem.used / (1024**3):.2f} GB ({mem.percent}%)")
    table.add_row("Memory Pressure", _get_pressure_emoji(mem.percent))
    table.add_row("Total Swap", f"{swap.total / (1024**3):.2f} GB")
    table.add_row("Used Swap", f"{swap.used / (1024**3):.2f} GB ({swap.percent}%)")
    table.add_row("SSD Internal Free", f"{disk.free / (1024**3):.2f} GB")

    # Thunderbolt disk info
    tb_path = Path(config.thunderbolt_disk)
    if tb_path.exists():
        tb_disk = psutil.disk_usage(str(tb_path))
        table.add_row("Thunderbolt SSD Total", f"{tb_disk.total / (1024**3):.2f} GB")
        table.add_row("Thunderbolt SSD Free", f"{tb_disk.free / (1024**3):.2f} GB")
    else:
        table.add_row("Thunderbolt SSD", "[red]Not connected[/red]")

    console.print(table)


@app.command("setup")
def setup(
    disk: str = typer.Option(
        config.thunderbolt_disk,
        "--disk",
        "-d",
        help="Path to Thunderbolt SSD",
    ),
    swap_size: str = typer.Option("64G", "--swap-size", "-s", help="Swap file size"),
) -> None:
    """Setup Thunderbolt SSD as memory extension."""
    script_path = Path(__file__).parent.parent.parent / "scripts" / "setup-thunderbolt-memory.sh"

    # If bundled, use the script from the same package
    if not script_path.exists():
        script_path = Path(__file__).parent / "setup-thunderbolt-memory.sh"

    if script_path.exists():
        result = run_command(
            ["bash", str(script_path), disk, swap_size],
            timeout=300,
        )
        console.print(result.stdout if result.success else result.stderr)
    else:
        console.print(
            Panel.fit(
                "[yellow]Setup script not found. Run the manual steps:[/yellow]\n\n"
                f"1. Connect your Thunderbolt 4 SSD to: {disk}\n"
                "2. Run: [cyan]sudo bash setup-thunderbolt-memory.sh {disk}[/cyan]\n\n"
                "Or download the script from: https://github.com/mateussiqueira/mac-thunderbolt-memory"
            )
        )


@app.command("monitor")
def monitor(
    interval: int = typer.Option(60, "--interval", "-i", help="Monitoring interval in seconds"),
) -> None:
    """Start memory monitoring daemon."""
    log_path = Path(config.thunderbolt_disk) / ".mac-memory-optimizer" / "logs" / "memory.log"

    if not log_path.exists():
        console.print(f"[yellow]⚠️  Monitor not configured. Run [cyan]omni memory setup[/cyan] first.[/yellow]")
        raise typer.Exit(1)

    console.print(f"[green]🚀 Starting memory monitor (interval: {interval}s)...[/green]")
    console.print(f"[dim]Press Ctrl+C to stop[/dim]")

    try:
        result = run_command(
            ["tail", "-f", str(log_path)],
            timeout=None,
        )
        console.print(result.stdout)
    except KeyboardInterrupt:
        console.print("\n[dim]Monitoring stopped.[/dim]")


@app.command("cache-move")
def cache_move(
    app_name: str = typer.Argument(..., help="Application cache to move (docker, npm, gradle, xcode)"),
    disk: str = typer.Option(config.thunderbolt_disk, "--disk", "-d", help="Thunderbolt SSD path"),
) -> None:
    """Move application caches to Thunderbolt SSD."""
    target_dir = Path(disk) / ".mac-memory-optimizer" / "apps" / app_name
    target_dir.mkdir(parents=True, exist_ok=True)

    moves = {
        "docker": (Path.home() / "Library" / "Containers" / "com.docker.docker", target_dir),
        "npm": (Path.home() / ".npm", target_dir),
        "gradle": (Path.home() / ".gradle", target_dir),
        "xcode": (Path.home() / "Library" / "Developer" / "Xcode" / "DerivedData", target_dir),
    }

    if app_name not in moves:
        console.print(f"[red]❌ Unknown app: {app_name}. Choose from: {', '.join(moves.keys())}[/red]")
        raise typer.Exit(1)

    source, target = moves[app_name]

    if not source.exists():
        console.print(f"[yellow]⚠️  Source not found: {source}[/yellow]")
        raise typer.Exit(1)

    console.print(f"[blue]📦 Moving {app_name} cache...[/blue]")
    console.print(f"   Source: {source}")
    console.print(f"   Target: {target}")

    # For safety, just show instructions instead of moving automatically
    console.print(
        Panel.fit(
            f"[bold]Manual steps to move {app_name} cache:[/bold]\n\n"
            f"1. [cyan]rsync -avh {source}/ {target}/[/cyan]\n"
            f"2. [cyan]mv {source} {source}.backup[/cyan]\n"
            f"3. [cyan]ln -s {target} {source}[/cyan]\n\n"
            "⚠️  [yellow]Make sure the app is closed before moving![/yellow]"
        )
    )


def _get_pressure_emoji(percent: float) -> str:
    """Return memory pressure with emoji."""
    if percent < 50:
        return f"🟢 Low ({percent}%)"
    elif percent < 80:
        return f"🟡 Medium ({percent}%)"
    elif percent < 95:
        return f"🟠 High ({percent}%)"
    else:
        return f"🔴 Critical ({percent}%)"
