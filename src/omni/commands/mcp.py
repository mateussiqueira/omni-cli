"""MCP (Model Context Protocol) commands for Omni CLI."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from omni.core.config import config
from omni.core.executor import run_command

app = typer.Typer(help="Manage MCP servers and tools")
console = Console()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """MCP management commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni MCP[/bold blue] - Use [cyan]omni mcp --help[/cyan]"))


@app.command("list")
def list_servers() -> None:
    """List configured MCP servers."""
    config_path = Path(config.mcp_config_path).expanduser()

    if not config_path.exists():
        console.print(f"[yellow]⚠️  MCP config not found at {config_path}[/yellow]")
        console.print("[dim]Set it with: export OMNI_MCP_CONFIG_PATH=/path/to/config[/dim]")
        return

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        servers = data.get("mcpServers", data.get("servers", {}))

        if not servers:
            console.print("[yellow]ℹ️  No MCP servers configured.[/yellow]")
            return

        table = Table(title="🔌 MCP Servers", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="cyan")
        table.add_column("Command", style="green")
        table.add_column("Args", style="yellow")

        for name, server_config in servers.items():
            cmd = server_config.get("command", "N/A")
            args = " ".join(server_config.get("args", []))[:50]
            table.add_row(name, cmd, args)

        console.print(table)

    except json.JSONDecodeError:
        console.print(f"[red]❌ Invalid JSON in {config_path}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


@app.command("add")
def add_server(
    name: str = typer.Argument(..., help="Server name"),
    command: str = typer.Argument(..., help="Command to run"),
    args: list[str] = typer.Argument(default_factory=list, help="Arguments for the command"),
) -> None:
    """Add a new MCP server."""
    config_path = Path(config.mcp_config_path).expanduser()
    config_path.parent.mkdir(parents=True, exist_ok=True)

    data = {"mcpServers": {}}
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            pass

    servers = data.setdefault("mcpServers", {})
    servers[name] = {"command": command, "args": args}

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    console.print(f"[green]✅ MCP server '{name}' added to {config_path}[/green]")


@app.command("remove")
def remove_server(
    name: str = typer.Argument(..., help="Server name to remove"),
) -> None:
    """Remove an MCP server."""
    config_path = Path(config.mcp_config_path).expanduser()

    if not config_path.exists():
        console.print("[yellow]⚠️  MCP config not found.[/yellow]")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    servers = data.get("mcpServers", data.get("servers", {}))

    if name not in servers:
        console.print(f"[yellow]⚠️  Server '{name}' not found.[/yellow]")
        return

    del servers[name]

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    console.print(f"[green]✅ MCP server '{name}' removed[/green]")


@app.command("test")
def test_server(
    name: str = typer.Argument(..., help="Server name to test"),
) -> None:
    """Test if an MCP server is reachable."""
    config_path = Path(config.mcp_config_path).expanduser()

    if not config_path.exists():
        console.print("[yellow]⚠️  MCP config not found.[/yellow]")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    servers = data.get("mcpServers", data.get("servers", {}))
    server = servers.get(name)

    if not server:
        console.print(f"[yellow]⚠️  Server '{name}' not found.[/yellow]")
        return

    cmd = [server["command"], *server.get("args", [])]

    console.print(f"[blue]🧪 Testing MCP server '{name}'...[/blue]")
    result = run_command(cmd, timeout=5)

    if result.success:
        console.print(f"[green]✅ Server '{name}' started successfully[/green]")
    else:
        console.print(f"[red]❌ Server '{name}' failed to start[/red]")
        console.print(f"[dim]{result.stderr[:500]}[/dim]")
