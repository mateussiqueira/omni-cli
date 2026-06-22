"""Shell completion commands for Omni CLI."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

from omni.core.executor import run_command

app = typer.Typer(help="Install shell completions")
console = Console()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Shell completion commands."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit("[bold blue]Omni Completion[/bold blue] - Use [cyan]omni completion --help[/cyan]"))


@app.command("bash")
def bash() -> None:
    """Show Bash completion installation instructions."""
    script_path = _get_completion_path("omni-completion.bash")

    console.print(Panel.fit("[bold]Bash Completion[/bold]\n"))
    console.print(f"Add this line to your [cyan]~/.bashrc[/cyan]:")
    console.print(f"\n  [green]source {script_path}[/green]\n")
    console.print("Or run:")
    console.print(f"  [cyan]echo 'source {script_path}' >> ~/.bashrc[/cyan]")


@app.command("zsh")
def zsh() -> None:
    """Show Zsh completion installation instructions."""
    script_path = _get_completion_path("omni-completion.zsh")

    console.print(Panel.fit("[bold]Zsh Completion[/bold]\n"))
    console.print(f"Copy the completion file to a directory in your [cyan]$fpath[/cyan]:")
    console.print(f"\n  [cyan]sudo cp {script_path} /usr/local/share/zsh/site-functions/_omni[/cyan]")
    console.print("\nEnsure the directory is in your [cyan]$fpath[/cyan]:")
    console.print("  [green]fpath+=/usr/local/share/zsh/site-functions[/green]")
    console.print("\nThen reload:")
    console.print("  [cyan]source ~/.zshrc[/cyan]")


@app.command("install")
def install(
    shell: str = typer.Argument(..., help="Shell to install completion for (bash, zsh)"),
) -> None:
    """Install shell completion automatically."""
    shell = shell.lower()

    if shell == "bash":
        script_path = _get_completion_path("omni-completion.bash")
        bashrc = Path.home() / ".bashrc"
        line = f"source {script_path}"

        with open(bashrc, "a+", encoding="utf-8") as f:
            f.seek(0)
            content = f.read()
            if line not in content:
                f.write(f"\n# Omni CLI completion\n{line}\n")

        console.print(f"[green]✅ Bash completion installed in {bashrc}[/green]")

    elif shell == "zsh":
        script_path = _get_completion_path("omni-completion.zsh")
        target_dir = Path("/usr/local/share/zsh/site-functions")
        target_file = target_dir / "_omni"

        if not target_dir.exists():
            console.print(f"[yellow]⚠️  Directory {target_dir} does not exist.[/yellow]")
            console.print("[dim]Please create it or install manually with:[/dim]")
            console.print(f"  [cyan]omni completion zsh[/cyan]")
            raise typer.Exit(1)

        result = run_command(["sudo", "cp", str(script_path), str(target_file)], timeout=30)
        if result.success:
            console.print(f"[green]✅ Zsh completion installed at {target_file}[/green]")
            console.print("[dim]Reload your shell with: source ~/.zshrc[/dim]")
        else:
            console.print(f"[red]❌ Failed to install Zsh completion[/red]")
            console.print(result.stderr)

    else:
        console.print(f"[red]❌ Unsupported shell: {shell}. Use 'bash' or 'zsh'.[/red]")
        raise typer.Exit(1)


def _get_completion_path(filename: str) -> str:
    """Get the absolute path to a completion script."""
    # When installed as editable package: src/omni/commands/completion.py -> project root
    package_dir = Path(__file__).parent.parent.parent.parent
    script_path = package_dir / "scripts" / "completion" / filename

    if script_path.exists():
        return str(script_path.resolve())

    # Fallback to installed location
    return str(Path.home() / ".local" / "share" / "omni-cli" / "completion" / filename)
