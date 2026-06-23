"""Main Omni CLI entrypoint."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from omni import __version__
from omni.commands import (
    aws,
    cloudflare,
    completion,
    config,
    github,
    hostinger,
    mcp,
    memory,
    plugins,
    unleash,
    update,
    vercel,
)
from omni.core.logger import audit_command, setup_audit_logging, setup_logging
from omni.core.plugins import register_plugins

# Setup logging early
logger = setup_logging()
setup_audit_logging()

app = typer.Typer(
    name="omni",
    help="A CLI das CLIs - Hub unificado para desenvolvimento",
    no_args_is_help=True,
    rich_markup_mode="rich",
)
console = Console()

# Register built-in subcommands
app.add_typer(memory.app, name="memory", help="🧠 Mac memory optimization")
app.add_typer(mcp.app, name="mcp", help="🔌 MCP server management")
app.add_typer(hostinger.app, name="hostinger", help="🌐 Hostinger domain/VPS management")
app.add_typer(github.app, name="github", help="🐙 GitHub repository management")
app.add_typer(unleash.app, name="unleash", help="🚦 Unleash feature flags")
app.add_typer(config.app, name="config", help="⚙️  Omni CLI configuration")
app.add_typer(completion.app, name="completion", help="🐚 Shell completion")
app.add_typer(plugins.app, name="plugins", help="🔌 Plugin management")
app.add_typer(update.app, name="update", help="🚀 Update Omni CLI")
app.add_typer(cloudflare.app, name="cloudflare", help="☁️  Cloudflare management")
app.add_typer(aws.app, name="aws", help="🌩️  AWS management")
app.add_typer(vercel.app, name="vercel", help="▲ Vercel management")

# Register external plugins automatically
register_plugins(app)


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
    ctx: typer.Context = typer.Option(None),
) -> None:
    """Omni CLI - A CLI das CLIs."""
    # Audit logging
    if ctx is not None and hasattr(ctx, "args"):
        try:
            import sys
            audit_command(sys.argv)
        except Exception:
            pass

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
