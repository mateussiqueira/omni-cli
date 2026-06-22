"""Configuration commands for Omni CLI."""

from __future__ import annotations

import os
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config

app = typer.Typer(help="Manage Omni CLI configuration")
console = Console()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Configuration commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Config[/bold blue] - Use [cyan]omni config --help[/cyan]"))


@app.command("show")
def show() -> None:
    """Show current configuration."""
    table = Table(title="⚙️  Omni CLI Configuration", show_header=True, header_style="bold magenta")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")

    for key, value in config.to_dict().items():
        # Mask sensitive values
        if "token" in key.lower() or "password" in key.lower():
            value = "***" if value else ""
        table.add_row(key, str(value))

    console.print(table)
    console.print(f"\n[dim]Config file: {config.config_file}[/dim]")


@app.command("set")
def set_config(
    key: str = typer.Argument(..., help="Configuration key"),
    value: str = typer.Argument(..., help="Configuration value"),
) -> None:
    """Set a configuration value."""
    if not hasattr(config, key):
        console.print(f"[red]❌ Unknown configuration key: {key}[/red]")
        raise typer.Exit(1)

    setattr(config, key, value)
    config.save_to_file()
    console.print(f"[green]✅ {key} updated[/green]")


@app.command("env")
def show_env() -> None:
    """Show environment variables to configure Omni CLI."""
    env_vars = [
        ("OMNI_HOSTINGER_API_TOKEN", "Hostinger API token"),
        ("OMNI_GITHUB_TOKEN", "GitHub personal access token"),
        ("OMNI_GITHUB_USERNAME", "GitHub username"),
        ("OMNI_UNLEASH_URL", "Unleash server URL"),
        ("OMNI_UNLEASH_API_TOKEN", "Unleash API token"),
        ("OMNI_MCP_CONFIG_PATH", "Path to MCP servers config"),
        ("OMNI_THUNDERBOLT_DISK", "Path to Thunderbolt SSD"),
    ]

    console.print(Panel.fit("[bold]Environment Variables[/bold]\n"))
    for var, desc in env_vars:
        current = os.environ.get(var, "")
        masked = "***" if current and ("TOKEN" in var or "PASSWORD" in var) else current
        console.print(f"[cyan]{var}[/cyan]")
        console.print(f"  [dim]{desc}[/dim]")
        console.print(f"  Current: [green]{masked or '(not set)'}[/green]\n")


@app.command("init")
def init() -> None:
    """Initialize Omni CLI configuration interactively."""
    console.print(Panel.fit("[bold blue]🚀 Omni CLI Initial Setup[/bold blue]"))

    config.hostinger_api_token = typer.prompt("Hostinger API token", default=config.hostinger_api_token, show_default=False)
    config.github_token = typer.prompt("GitHub token", default=config.github_token, show_default=False)
    config.github_username = typer.prompt("GitHub username", default=config.github_username)
    config.unleash_url = typer.prompt("Unleash URL", default=config.unleash_url)
    config.unleash_api_token = typer.prompt("Unleash API token", default=config.unleash_api_token, show_default=False)
    config.thunderbolt_disk = typer.prompt("Thunderbolt SSD path", default=config.thunderbolt_disk)

    config.save_to_file()
    console.print(f"\n[green]✅ Configuration saved to {config.config_file}[/green]")
