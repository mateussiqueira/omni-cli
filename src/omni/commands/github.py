"""GitHub commands for Omni CLI."""

from __future__ import annotations

from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config

app = typer.Typer(help="GitHub repository and workflow management")
console = Console()

GITHUB_API_BASE = "https://api.github.com"


def _get_headers() -> dict[str, str]:
    """Get GitHub API headers."""
    if not config.github_token:
        console.print("[red]❌ GitHub token not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_GITHUB_TOKEN=your_token[/dim]")
        raise typer.Exit(1)

    return {
        "Authorization": f"Bearer {config.github_token}",
        "Accept": "application/vnd.github.v3+json",
    }


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """GitHub management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni GitHub[/bold blue] - Use [cyan]omni github --help[/cyan]"))


@app.command("repos")
def list_repos(
    username: Optional[str] = typer.Option(None, "--user", "-u", help="GitHub username"),
) -> None:
    """List GitHub repositories."""
    user = username or config.github_username

    if not user:
        console.print("[red]❌ GitHub username not configured.[/red]")
        console.print("[dim]Set it with: export OMNI_GITHUB_USERNAME=your_user[/dim]")
        raise typer.Exit(1)

    try:
        response = httpx.get(
            f"{GITHUB_API_BASE}/users/{user}/repos?sort=updated&per_page=20",
            headers=_get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        repos = response.json()

        table = Table(title=f"📦 GitHub Repos: {user}", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Language", style="green")
        table.add_column("Stars", style="yellow")
        table.add_column("Updated", style="blue")

        for repo in repos:
            table.add_row(
                repo.get("name", "N/A"),
                repo.get("language") or "N/A",
                str(repo.get("stargazers_count", 0)),
                repo.get("updated_at", "N/A")[:10],
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("trending")
def trending(
    language: Optional[str] = typer.Option(None, "--lang", "-l", help="Filter by language"),
) -> None:
    """Show trending GitHub repositories."""
    url = f"{GITHUB_API_BASE}/search/repositories?q=stars:>1000&sort=stars&order=desc&per_page=10"
    if language:
        url = f"{GITHUB_API_BASE}/search/repositories?q=stars:>1000+language:{language}&sort=stars&order=desc&per_page=10"

    try:
        response = httpx.get(url, headers=_get_headers(), timeout=30)
        response.raise_for_status()
        repos = response.json().get("items", [])

        table = Table(title="🔥 Trending GitHub Repos", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Language", style="green")
        table.add_column("Stars", style="yellow")
        table.add_column("Description", style="white")

        for repo in repos:
            desc = (repo.get("description") or "")[:60]
            table.add_row(
                repo.get("full_name", "N/A"),
                repo.get("language") or "N/A",
                f"⭐ {repo.get('stargazers_count', 0):,}",
                desc,
            )

        console.print(table)

    except httpx.HTTPError as e:
        console.print(f"[red]❌ API error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("clone")
def clone(
    repo: str = typer.Argument(..., help="Repository to clone (owner/repo)"),
    directory: Optional[str] = typer.Option(None, "--dir", "-d", help="Target directory"),
) -> None:
    """Clone a GitHub repository."""
    from omni.core.executor import run_command

    url = f"https://github.com/{repo}.git"
    cmd = ["git", "clone", url]
    if directory:
        cmd.append(directory)

    console.print(f"[blue]📥 Cloning {repo}...[/blue]")
    result = run_command(cmd, timeout=120)

    if result.success:
        console.print(f"[green]✅ Repository cloned successfully[/green]")
    else:
        console.print(f"[red]❌ Failed to clone repository[/red]")
        console.print(result.stderr)
