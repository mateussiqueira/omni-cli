"""Self-update command for Omni CLI."""

from __future__ import annotations

import sys

import httpx
import typer
from rich.console import Console
from rich.panel import Panel

from omni import __version__
from omni.core.executor import run_command

app = typer.Typer(help="Update Omni CLI to the latest version")
console = Console()

PYPI_API_URL = "https://pypi.org/pypi/omni-cli/json"


@app.callback(invoke_without_command=True)
def main(
    check: bool = typer.Option(False, "--check", "-c", help="Check for updates without installing"),
    force: bool = typer.Option(False, "--force", "-f", help="Force reinstall"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Show what would be done"),
) -> None:
    """Update Omni CLI to the latest version."""
    console.print(Panel.fit("[bold blue]🚀 Omni CLI Self-Update[/bold blue]"))

    current_version = __version__
    latest_version = get_latest_version()

    if not latest_version:
        console.print("[red]❌ Could not check for updates. Please try again later.[/red]")
        raise typer.Exit(1)

    console.print(f"[dim]Current version:[/dim] [cyan]{current_version}[/cyan]")
    console.print(f"[dim]Latest version:[/dim]  [cyan]{latest_version}[/cyan]")

    if not force and current_version == latest_version:
        console.print("[green]✅ Omni CLI is already up to date![/green]")
        return

    if check:
        if current_version != latest_version:
            console.print(f"[yellow]⚠️  Update available: {latest_version}[/yellow]")
            console.print("[dim]Run [cyan]omni update[/cyan] to install.[/dim]")
        return

    if dry_run:
        console.print(f"[blue]🔍 Would run: pip install --upgrade {'--force-reinstall ' if force else ''}omni-cli[/blue]")
        return

    # Determine pip command
    pip_cmd = sys.executable.replace("python", "pip") if "python" in sys.executable else "pip"

    console.print(f"[blue]📦 Installing Omni CLI {latest_version}...[/blue]")

    cmd = [pip_cmd, "install", "--upgrade"]
    if force:
        cmd.append("--force-reinstall")
    cmd.append("omni-cli")

    result = run_command(cmd, timeout=180)

    if result.success:
        console.print(f"[green]✅ Omni CLI updated to {latest_version}[/green]")
        console.print("[dim]Restart your terminal to use the new version.[/dim]")
    else:
        console.print("[red]❌ Update failed[/red]")
        console.print(result.stderr)
        raise typer.Exit(1)


def get_latest_version() -> str | None:
    """Fetch the latest version of Omni CLI from PyPI."""
    try:
        response = httpx.get(PYPI_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except Exception:
        return None
