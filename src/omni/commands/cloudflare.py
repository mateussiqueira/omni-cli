"""Cloudflare management commands for Omni CLI."""

from __future__ import annotations

from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config

app = typer.Typer(help="Manage Cloudflare DNS and zones")
console = Console()

CLOUDFLARE_API_BASE = "https://api.cloudflare.com/client/v4"


def _get_headers() -> dict[str, str]:
    """Get Cloudflare API headers."""
    token = config.cloudflare_api_token or ""
    if not token:
        console.print("[red]❌ Cloudflare API token not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_CLOUDFLARE_API_TOKEN=your_token[/dim]")
        raise typer.Exit(1)

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Cloudflare management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Cloudflare[/bold blue] - Use [cyan]omni cloudflare --help[/cyan]"))


@app.command("zones")
def list_zones() -> None:
    """List Cloudflare zones."""
    try:
        response = httpx.get(
            f"{CLOUDFLARE_API_BASE}/zones",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        if not data.get("success"):
            console.print(f"[red]❌ API error: {data.get('errors', [])}[/red]")
            return

        zones = data.get("result", [])

        table = Table(title="☁️  Cloudflare Zones", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("ID", style="green")
        table.add_column("Status", style="yellow")

        for zone in zones:
            table.add_row(
                zone.get("name", "N/A"),
                zone.get("id", "N/A")[:20] + "...",
                zone.get("status", "N/A"),
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")


@app.command("dns")
def list_dns(
    zone_name: str = typer.Argument(..., help="Zone name (domain)"),
) -> None:
    """List DNS records for a Cloudflare zone."""
    try:
        # First get zone ID
        zones_response = httpx.get(
            f"{CLOUDFLARE_API_BASE}/zones",
            headers=_get_headers(),
            params={"name": zone_name},
            timeout=30,
        )
        zones_response.raise_for_status()
        zones_data = zones_response.json()

        if not zones_data.get("success") or not zones_data.get("result"):
            console.print(f"[red]❌ Zone '{zone_name}' not found[/red]")
            return

        zone_id = zones_data["result"][0]["id"]

        response = httpx.get(
            f"{CLOUDFLARE_API_BASE}/zones/{zone_id}/dns_records",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        records = data.get("result", [])

        table = Table(title=f"📋 Cloudflare DNS: {zone_name}", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Type", style="green")
        table.add_column("Content", style="yellow")
        table.add_column("TTL", style="blue")

        for record in records:
            table.add_row(
                record.get("name", "N/A"),
                record.get("type", "A"),
                record.get("content", "N/A"),
                str(record.get("ttl", "N/A")),
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")


@app.command("purge")
def purge_cache(
    zone_name: str = typer.Argument(..., help="Zone name (domain)"),
) -> None:
    """Purge Cloudflare cache for a zone."""
    try:
        zones_response = httpx.get(
            f"{CLOUDFLARE_API_BASE}/zones",
            headers=_get_headers(),
            params={"name": zone_name},
            timeout=30,
        )
        zones_response.raise_for_status()
        zones_data = zones_response.json()

        if not zones_data.get("success") or not zones_data.get("result"):
            console.print(f"[red]❌ Zone '{zone_name}' not found[/red]")
            return

        zone_id = zones_data["result"][0]["id"]

        response = httpx.post(
            f"{CLOUDFLARE_API_BASE}/zones/{zone_id}/purge_cache",
            headers=_get_headers(),
            json={"purge_everything": True},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        if data.get("success"):
            console.print(f"[green]✅ Cache purged for {zone_name}[/green]")
        else:
            console.print(f"[red]❌ Failed to purge cache: {data.get('errors', [])}[/red]")

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
