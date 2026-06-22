# Architecture

This document describes the architecture of **Omni CLI**.

## Design Principles

1. **Modularity**: Each tool/domain has its own command module
2. **Extensibility**: New commands can be added without modifying existing code
3. **Configuration**: Centralized configuration via environment variables and config file
4. **Testability**: Commands are decoupled from CLI framework

## Project Structure

```text
omni-cli/
├── src/omni/
│   ├── __init__.py         # Package metadata
│   ├── cli.py              # Main Typer application and entrypoint
│   ├── commands/           # Domain-specific command modules
│   │   ├── __init__.py
│   │   ├── memory.py       # macOS memory optimization
│   │   ├── mcp.py          # MCP server management
│   │   ├── hostinger.py    # Hostinger API integration
│   │   ├── github.py       # GitHub API integration
│   │   ├── unleash.py      # Unleash API integration
│   │   └── config.py       # Configuration management
│   └── core/               # Shared utilities
│       ├── __init__.py
│       ├── config.py       # OmniConfig class (Pydantic)
│       └── executor.py     # Shell command executor
├── tests/                  # Unit tests
├── docs/                   # Documentation (EN & PT)
├── pyproject.toml          # Project metadata and tool config
└── README.md               # Main documentation (English)
```

## Core Components

### `omni.core.config.OmniConfig`

Uses Pydantic Settings to manage configuration from:
- Environment variables (prefix `OMNI_`)
- `~/.config/omni/config.toml`
- Default values

### `omni.core.executor.run_command`

A utility to execute shell commands safely, returning a structured result with:
- Return code
- stdout
- stderr
- Success flag

### `omni.cli.app`

The main Typer application that registers all command modules via `add_typer()`.

## Adding a New Command

To add a new command group:

1. Create `src/omni/commands/new_tool.py`
2. Define a Typer app:

```python
import typer

app = typer.Typer(help="Description of new tool")

@app.command("hello")
def hello() -> None:
    print("Hello from new tool!")
```

3. Register in `src/omni/cli.py`:

```python
from omni.commands import new_tool
app.add_typer(new_tool.app, name="new-tool", help="New tool commands")
```

## Testing

Tests use Typer's `CliRunner` to invoke commands without running subprocesses.

```python
from typer.testing import CliRunner
from omni.cli import app

runner = CliRunner()
result = runner.invoke(app, ["version"])
assert result.exit_code == 0
```

## Future Enhancements

- Plugin system for external command packs
- Shell completion scripts
- Configuration profiles
- Encrypted credential storage
- Web dashboard for monitoring
