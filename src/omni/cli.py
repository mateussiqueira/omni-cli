"""Main Omni CLI entrypoint."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from omni import __version__
from omni.commands import config, github, hostinger, mcp, memory, unleash

app = typer.Typer(
    name="omni",
    help="A CLI das CLIs - Hub unificado para desenvolvimento",
    no_args_is_help=True,
    rich_markup_mode="rich",
)
console = Console()

# Register subcommands
app.add_typer(memory.app, name="memory", help="🧠 Mac memory optimization")
app.add_typer(mcp.app, name="mcp", help="🔌 MCP server management")
app.add_typer(hostinger.app, name="hostinger", help="🌐 Hostinger domain/VPS management")
app.add_typer(github.app, name="github", help="🐙 GitHub repository management")
app.add_typer(unleash.app, name="unleash", help="🚦 Unleash feature flags")
app.add_typer(config.app, name="config", help="⚙️  Omni CLI configuration")


@app.command("version")
def version() -> None:
    """Show Omni CLI version."""
    console.print(f"[bold blue]Omni CLI[/bold blue] version [green]{__version__}[/green]")


@app.command("status")
def status() -> None:
    """Show overall system status."""
    console.print(Panel.fit("[bold blue]🌟 Omni CLI Status[/bold blue]"))
    console.print("[green]✅ Omni CLI is ready to use![/green]")
    console.print("\n[dim]Available commands:[/dim]")
    console.print("  [cyan]omni memory status[/cyan]    - Check Mac memory status")
    console.print("  [cyan]omni mcp list[/cyan]         - List MCP servers")
    console.print("  [cyan]omni hostinger domains[/cyan]- List Hostinger domains")
    console.print("  [cyan]omni github repos[/cyan]     - List GitHub repositories")
    console.print("  [cyan]omni unleash flags[/cyan]    - List Unleash feature flags")
    console.print("  [cyan]omni config init[/cyan]      - Initial setup")


@app.callback()
def main(
    version_flag: bool = typer.Option(False, "--version", "-v", help="Show version"),
) -> None:
    """Omni CLI - A CLI das CLIs."""
    if version_flag:
        typer.echo(f"Omni CLI {__version__}")
        raise typer.Exit()


def _print_banner() -> None:
    """Print Omni CLI banner."""
    banner = Text()
    banner.append("  ██████  ███    ███ ██ ███    ██\n", style="bold blue")
    banner.append(" ██    ██ ████  ████ ██ ████   ██\n", style="bold blue")
    banner.append(" ██    ██ ██ ████ ██ ██ ██ ██  ██\n", style="bold cyan")
    banner.append(" ██    ██ ██  ██  ██ ██ ██  ██ ██\n", style="bold cyan")
    banner.append("  ██████  ██      ██ ██ ██   ████\n", style="bold magenta")
    banner.append("\n     A CLI das CLIs v" + __version__ + "\n", style="dim")
    console.print(banner)


if __name__ == "__main__":
    _print_banner()
    app()
