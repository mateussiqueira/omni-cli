"""Vercel management commands for Omni CLI."""

from __future__ import annotations

from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config

app = typer.Typer(help="Manage Vercel projects and deployments")
console = Console()

VERCEL_API_BASE = "https://api.vercel.com"


def _get_headers() -> dict[str, str]:
    """Get Vercel API headers."""
    token = config.vercel_token or ""
    if not token:
        console.print("[red]❌ Vercel token not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_VERCEL_TOKEN=your_token[/dim]")
        raise typer.Exit(1)

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Vercel management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Vercel[/bold blue] - Use [cyan]omni vercel --help[/cyan]"))


@app.command("projects")
def list_projects() -> None:
    """List Vercel projects."""
    try:
        response = httpx.get(
            f"{VERCEL_API_BASE}/v9/projects",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        projects = data.get("projects", [])

        table = Table(title="▲ Vercel Projects", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Framework", style="green")
        table.add_column("Latest Deployment", style="yellow")

        for project in projects:
            latest = project.get("latestDeployments", [{}])[0]
            table.add_row(
                project.get("name", "N/A"),
                project.get("framework", "N/A"),
                latest.get("url", "N/A") if latest else "N/A",
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")


@app.command("deployments")
def list_deployments(
    project: Optional[str] = typer.Option(None, "--project", "-p", help="Project name"),
    limit: int = typer.Option(10, "--limit", "-l", help="Number of deployments to show"),
) -> None:
    """List Vercel deployments."""
    try:
        params: dict[str, str | int] = {"limit": limit}
        if project:
            params["projectId"] = project

        response = httpx.get(
            f"{VERCEL_API_BASE}/v6/deployments",
            headers=_get_headers(),
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        deployments = data.get("deployments", [])

        table = Table(title="▲ Vercel Deployments", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("State", style="green")
        table.add_column("URL", style="yellow")
        table.add_column("Created", style="blue")

        for deployment in deployments:
            state = deployment.get("state", "N/A")
            state_color = "green" if state == "READY" else "yellow" if state == "BUILDING" else "red"
            table.add_row(
                deployment.get("name", "N/A"),
                f"[{state_color}]{state}[/{state_color}]",
                deployment.get("url", "N/A"),
                deployment.get("createdAt", "N/A")[:10],
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")


@app.command("env")
def list_env(
    project: str = typer.Argument(..., help="Project name or ID"),
) -> None:
    """List environment variables for a Vercel project."""
    try:
        response = httpx.get(
            f"{VERCEL_API_BASE}/v9/projects/{project}/env",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        env_vars = data.get("envs", [])

        table = Table(title=f"▲ Vercel Env: {project}", show_header=True, header_style="bold magenta")
        table.add_column("Key", style="cyan")
        table.add_column("Target", style="green")
        table.add_column("Type", style="yellow")

        for env in env_vars:
            targets = ", ".join(env.get("target", []))
            table.add_row(
                env.get("key", "N/A"),
                targets,
                env.get("type", "plain"),
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
