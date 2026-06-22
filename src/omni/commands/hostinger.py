"""Hostinger management commands for Omni CLI."""

from __future__ import annotations

from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config

app = typer.Typer(help="Manage Hostinger domains, VPS and DNS")
console = Console()

HOSTINGER_API_BASE = "https://developers.hostinger.com"


def _get_headers() -> dict[str, str]:
    """Get Hostinger API headers."""
    if not config.hostinger_api_token:
        console.print("[red]❌ Hostinger API token not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_HOSTINGER_API_TOKEN=your_token[/dim]")
        raise typer.Exit(1)

    return {
        "Authorization": f"Bearer {config.hostinger_api_token}",
        "Content-Type": "application/json",
    }


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Hostinger management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Hostinger[/bold blue] - Use [cyan]omni hostinger --help[/cyan]"))


@app.command("domains")
def list_domains() -> None:
    """List Hostinger domains."""
    try:
        response = httpx.get(
            f"{HOSTINGER_API_BASE}/api/domains/v1/domains",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        domains = response.json()

        table = Table(title="🌐 Hostinger Domains", show_header=True, header_style="bold magenta")
        table.add_column("Domain", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Nameservers", style="yellow")

        for domain in domains:
            ns = f"{domain.get('name_servers', {}).get('ns1', 'N/A')}, {domain.get('name_servers', {}).get('ns2', 'N/A')}"
            table.add_row(
                domain.get("domain", "N/A"),
                domain.get("status", "N/A"),
                ns,
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("vps")
def list_vps() -> None:
    """List Hostinger VPS instances."""
    try:
        response = httpx.get(
            f"{HOSTINGER_API_BASE}/api/vps/v1/virtual-machines",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        vms = response.json()

        table = Table(title="🖥️  Hostinger VPS", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="cyan")
        table.add_column("Hostname", style="green")
        table.add_column("IP", style="yellow")
        table.add_column("Status", style="blue")

        for vm in vms:
            ip = vm.get("ipv4", [{}])[0].get("address", "N/A") if vm.get("ipv4") else "N/A"
            table.add_row(
                str(vm.get("id", "N/A")),
                vm.get("hostname", "N/A"),
                ip,
                vm.get("state", "N/A"),
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("dns")
def get_dns(
    domain: str = typer.Argument(..., help="Domain to query DNS records"),
) -> None:
    """Get DNS records for a domain."""
    try:
        response = httpx.get(
            f"{HOSTINGER_API_BASE}/api/dns/v1/domains/{domain}/records",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        records = response.json()

        table = Table(title=f"📋 DNS Records: {domain}", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Type", style="green")
        table.add_column("Value", style="yellow")
        table.add_column("TTL", style="blue")

        for record in records:
            for r in record.get("records", []):
                table.add_row(
                    record.get("name", "@"),
                    record.get("type", "A"),
                    r.get("content", "N/A"),
                    str(record.get("ttl", "N/A")),
                )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
