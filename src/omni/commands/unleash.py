"""Unleash feature flag commands for Omni CLI."""

from __future__ import annotations

from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config

app = typer.Typer(help="Manage Unleash feature flags")
console = Console()


def _get_headers() -> dict[str, str]:
    """Get Unleash API headers."""
    if not config.unleash_api_token:
        console.print("[red]❌ Unleash API token not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_UNLEASH_API_TOKEN=your_token[/dim]")
        raise typer.Exit(1)

    return {
        "Authorization": config.unleash_api_token,
        "Content-Type": "application/json",
    }


def _get_base_url() -> str:
    """Get Unleash base URL."""
    if not config.unleash_url:
        console.print("[red]❌ Unleash URL not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_UNLEASH_URL=https://your-unleash.com[/dim]")
        raise typer.Exit(1)

    return config.unleash_url.rstrip("/")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Unleash management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Unleash[/bold blue] - Use [cyan]omni unleash --help[/cyan]"))


@app.command("flags")
def list_flags(
    project: Optional[str] = typer.Option("default", "--project", "-p", help="Project ID"),
) -> None:
    """List Unleash feature flags."""
    try:
        response = httpx.get(
            f"{_get_base_url()}/api/admin/projects/{project}/features",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        flags = data.get("features", data if isinstance(data, list) else [])

        table = Table(title=f"🚦 Unleash Flags: {project}", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Type", style="green")
        table.add_column("Enabled", style="yellow")
        table.add_column("Created", style="blue")

        for flag in flags:
            enabled = "🟢 Yes" if flag.get("enabled") else "🔴 No"
            table.add_row(
                flag.get("name", "N/A"),
                flag.get("type", "release"),
                enabled,
                flag.get("createdAt", "N/A")[:10],
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("toggle")
def toggle_flag(
    flag_name: str = typer.Argument(..., help="Feature flag name"),
    enabled: bool = typer.Argument(..., help="Enable or disable"),
    project: str = typer.Option("default", "--project", "-p", help="Project ID"),
) -> None:
    """Enable or disable a feature flag."""
    try:
        action = "enable" if enabled else "disable"
        response = httpx.post(
            f"{_get_base_url()}/api/admin/projects/{project}/features/{flag_name}/{action}",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()

        status = "enabled" if enabled else "disabled"
        console.print(f"[green]✅ Feature flag '{flag_name}' {status}[/green]")

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("create")
def create_flag(
    name: str = typer.Argument(..., help="Feature flag name"),
    description: Optional[str] = typer.Option(None, "--desc", "-d", help="Flag description"),
    project: str = typer.Option("default", "--project", "-p", help="Project ID"),
) -> None:
    """Create a new feature flag."""
    payload = {
        "name": name,
        "description": description or f"Flag created by Omni CLI",
        "type": "release",
        "impressionData": False,
    }

    try:
        response = httpx.post(
            f"{_get_base_url()}/api/admin/projects/{project}/features",
            headers=_get_headers(),
            json=payload,
            timeout=30,
        )
        response.raise_for_status()

        console.print(f"[green]✅ Feature flag '{name}' created[/green]")

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
