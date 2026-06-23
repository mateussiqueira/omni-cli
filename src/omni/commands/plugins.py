"""Plugin management commands for Omni CLI."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.executor import run_command
from omni.core.plugins import list_plugins

app = typer.Typer(help="Manage Omni CLI plugins")
console = Console()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Plugin management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Plugins[/bold blue] - Use [cyan]omni plugins --help[/cyan]"))


@app.command("list")
def list_cmd() -> None:
    """List installed Omni CLI plugins."""
    plugins = list_plugins()

    if not plugins:
        console.print("[yellow]ℹ️  No plugins installed.[/yellow]")
        console.print("[dim]Install plugins with: pip install omni-cli-<plugin-name>[/dim]")
        return

    table = Table(title="🔌 Omni CLI Plugins", show_header=True, header_style="bold magenta")
    table.add_column("Name", style="cyan")
    table.add_column("Package", style="green")
    table.add_column("Version", style="yellow")
    table.add_column("Module", style="blue")

    for plugin in plugins:
        table.add_row(
            plugin.get("name", "N/A"),
            plugin.get("package", "N/A"),
            plugin.get("version", "N/A"),
            plugin.get("module", "N/A"),
        )

    console.print(table)


@app.command("search")
def search(
    query: str = typer.Argument("omni-cli-", help="Search query for plugins"),
) -> None:
    """Search for Omni CLI plugins on PyPI."""
    console.print(f"[blue]🔍 Searching PyPI for plugins matching '{query}'...[/blue]")
    result = run_command(["pip", "search", query], timeout=30)

    if result.success:
        console.print(result.stdout)
    else:
        console.print("[yellow]⚠️  pip search is disabled on PyPI.[/yellow]")
        console.print("[dim]Visit https://pypi.org/search/?q=omni-cli- to find plugins.[/dim]")


@app.command("install")
def install(
    package: str = typer.Argument(..., help="Plugin package name to install"),
) -> None:
    """Install an Omni CLI plugin."""
    console.print(f"[blue]📦 Installing plugin: {package}...[/blue]")
    result = run_command(["pip", "install", package], timeout=120)

    if result.success:
        console.print(f"[green]✅ Plugin '{package}' installed successfully[/green]")
        console.print("[dim]Restart your terminal to load the new plugin.[/dim]")
    else:
        console.print(f"[red]❌ Failed to install plugin '{package}'[/red]")
        console.print(result.stderr)


@app.command("uninstall")
def uninstall(
    package: str = typer.Argument(..., help="Plugin package name to uninstall"),
) -> None:
    """Uninstall an Omni CLI plugin."""
    console.print(f"[blue]🗑️  Uninstalling plugin: {package}...[/blue]")
    result = run_command(["pip", "uninstall", "-y", package], timeout=60)

    if result.success:
        console.print(f"[green]✅ Plugin '{package}' uninstalled successfully[/green]")
    else:
        console.print(f"[red]❌ Failed to uninstall plugin '{package}'[/red]")
        console.print(result.stderr)


@app.command("create")
def create(
    name: str = typer.Argument(..., help="Plugin name"),
) -> None:
    """Create a new Omni CLI plugin template."""
    import os
    from pathlib import Path

    plugin_dir = Path(f"omni-cli-{name}")
    if plugin_dir.exists():
        console.print(f"[red]❌ Directory {plugin_dir} already exists[/red]")
        raise typer.Exit(1)

    package_name = f"omni_{name.replace('-', '_')}"
    src_dir = plugin_dir / "src" / package_name
    src_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    (src_dir / "__init__.py").write_text(
        f'"""Omni CLI {name} plugin."""\n\nfrom .commands import app\n\n__version__ = "0.1.0"\n\n__all__ = ["app"]\n'
    )

    # Create commands.py
    (src_dir / "commands.py").write_text(
        f'''"""Commands for Omni CLI {name} plugin."""

import typer
from rich.console import Console

app = typer.Typer(help="{name} plugin commands")
console = Console()


@app.command("hello")
def hello() -> None:
    """Say hello from {name} plugin."""
    console.print("[green]Hello from {name} plugin![/green]")
'''
    )

    # Create pyproject.toml
    (plugin_dir / "pyproject.toml").write_text(
        f'''[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "omni-cli-{name}"
version = "0.1.0"
description = "Omni CLI plugin for {name}"
requires-python = ">=3.10"
dependencies = [
    "omni-cli>=0.1.0",
]

[project.entry-points."omni.plugins"]
{name} = "{package_name}:app"

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
]

[tool.hatch.build.targets.wheel]
packages = ["src/{package_name}"]
'''
    )

    # Create README
    (plugin_dir / "README.md").write_text(
        f'''# Omni CLI {name} Plugin

Plugin for Omni CLI.

## Installation

```bash
pip install omni-cli-{name}
```

## Usage

```bash
omni {name} hello
```
'''
    )

    console.print(f"[green]✅ Plugin template created in {plugin_dir}/[/green]")
    console.print(f"[dim]Next steps:[/dim]")
    console.print(f"  [cyan]cd {plugin_dir}[/cyan]")
    console.print(f"  [cyan]pip install -e .[/cyan]")
    console.print(f"  [cyan]omni {name} hello[/cyan]")
