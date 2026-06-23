# Architecture

This document describes the architecture of **Omni CLI** — a modular, extensible command-line hub that unifies development tools under a single interface.

## Design Principles

1. **Modularity**: Each tool/domain has its own command module
2. **Extensibility**: New commands can be added without modifying existing code
3. **Configuration**: Centralized configuration via environment variables and config file
4. **Testability**: Commands are decoupled from the CLI framework
5. **Plugin-first**: External plugins can extend functionality via Python entry points

## Project Structure

```text
omni-cli/
├── src/omni/
│   ├── __init__.py         # Package metadata (version, author, license)
│   ├── cli.py              # Main Typer application and entrypoint
│   ├── commands/           # Domain-specific command modules (12 groups)
│   │   ├── __init__.py
│   │   ├── memory.py       # macOS memory optimization via Thunderbolt SSD
│   │   ├── mcp.py          # MCP (Model Context Protocol) server management
│   │   ├── hostinger.py    # Hostinger API integration (domains, DNS, VPS)
│   │   ├── github.py       # GitHub API integration (repos, trending)
│   │   ├── unleash.py      # Unleash feature flag management
│   │   ├── cloudflare.py   # Cloudflare API integration (DNS, cache)
│   │   ├── aws.py          # AWS operations (S3, EC2, Route53)
│   │   ├── vercel.py       # Vercel project and deployment management
│   │   ├── config.py       # Configuration management commands
│   │   ├── completion.py   # Shell completion (bash, zsh)
│   │   ├── plugins.py      # Plugin management (install, list, remove)
│   │   └── update.py       # Self-update from PyPI
│   └── core/               # Shared framework utilities
│       ├── __init__.py
│       ├── config.py       # OmniConfig class (Pydantic Settings)
│       ├── executor.py     # Shell command executor with structured results
│       ├── logger.py       # Logging and audit trail system
│       ├── plugins.py      # Plugin discovery via entry points
│       └── profiles.py     # Named profile management (dev/staging/prod)
├── tests/                  # Unit tests (pytest + CliRunner)
├── docs/                   # Documentation (English + Portuguese)
├── assets/                 # Logos, banner, favicon
├── scripts/                # Utility scripts
│   ├── generate_logo.py    # Logo/banner asset generator
│   └── completion/         # Shell completion scripts
├── mkdocs.yml              # Documentation site config
├── pyproject.toml          # Project metadata and tool config
├── Makefile                # Dev targets (test, lint, build)
├── README.md               # Main README (English)
├── README.pt.md            # README (Portuguese)
├── CHANGELOG.md            # Version changelog
└── LICENSE                 # MIT license
```

## Core Components

### `omni.cli.app` (Entrypoint)

The main Typer application (`src/omni/cli.py`) is the single entrypoint for all Omni CLI operations. It:

- Registers 12 built-in command groups via `app.add_typer()`
- Registers external plugins discovered at runtime via `register_plugins()`
- Provides global `version` and `status` commands
- Sets up audit logging for every command invocation

### `omni.core.config.OmniConfig`

Uses Pydantic Settings to manage configuration from three sources (in order of precedence):

1. **Environment variables** with prefix `OMNI_` (e.g., `OMNI_GITHUB_TOKEN`)
2. **Config file** at `~/.config/omni/config.toml`
3. **Default values** defined in the model

Supports named profiles (dev/staging/prod) with isolated credentials per profile.

### `omni.core.executor.run_command`

A utility to execute shell commands safely, returning a structured `CommandResult`:

```python
@dataclass
class CommandResult:
    return_code: int
    stdout: str
    stderr: str
    success: bool
```

### `omni.core.logger`

Two-tier logging system:

- **Application logging**: Standard Python logging to `~/.config/omni/logs/omni.log`
- **Audit trail**: JSON-structured audit log of every command, stored at `$OMNI_AUDIT_LOG` or `~/.config/omni/audit/omni-audit.log`

### `omni.core.plugins`

Uses Python's `importlib.metadata.entry_points` (group: `omni.plugins`) to discover and register external command groups at runtime. Plugins can be installed via pip and are automatically loaded.

### `omni.core.profiles`

Manages named configuration profiles:

- Switch between dev, staging, and production with `omni config profile switch <name>`
- Each profile has its own set of credentials
- Profiles stored in `~/.config/omni/profiles/`

## Command Registration Flow

```
User input → omni <group> <command> [args]
                   │
                   ▼
         omni.cli.main() ←─── audit_command()
                   │
                   ▼
         app() [Typer]
                   │
          ┌────────┴────────┐
          ▼                  ▼
   Built-in groups     External plugins
   (add_typer)         (entry_points)
          │                  │
          ▼                  ▼
   Command function → rich.console output
```

## Adding a New Command

1. Create `src/omni/commands/new_tool.py`:

```python
import typer

app = typer.Typer(help="Description of new tool")

@app.command("hello")
def hello() -> None:
    """Say hello from new tool."""
    print("Hello from new tool!")
```

2. Register in `src/omni/cli.py`:

```python
from omni.commands import new_tool

app.add_typer(new_tool.app, name="new-tool", help="New tool commands")
```

## Adding a Plugin

1. Create a separate Python package with an entry point in `pyproject.toml`:

```toml
[project.entry-points."omni.plugins"]
my-plugin = "my_plugin:app"
```

2. The plugin's `app` must be a Typer instance. It will be automatically discovered and registered when Omni CLI starts.

## Testing

Tests use Typer's `CliRunner` to invoke commands without running subprocesses:

```python
from typer.testing import CliRunner
from omni.cli import app

runner = CliRunner()
result = runner.invoke(app, ["version"])
assert result.exit_code == 0
```

Run tests with:

```bash
make test
# or
pytest --cov=omni --cov-report=term-missing
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `typer` | CLI framework |
| `rich` | Terminal output (tables, panels, colors) |
| `pydantic` + `pydantic-settings` | Configuration models |
| `click` | Typer dependency, shell completion |
| `httpx` + `requests` | HTTP clients for API integrations |
| `psutil` | System metrics (memory, CPU) |
| `toml` / `pyyaml` | Config file parsing |

## Security

- No secrets are stored in code — all credentials come from environment variables or encrypted config
- Audit trail logs all commands for accountability
- Config file permissions: `600` (owner read/write only)

## Future Enhancements

- Encrypted credential storage (keyring integration)
- Web dashboard for monitoring
- More cloud integrations (DigitalOcean, Hetzner, GCP)
- Homebrew formula for macOS
- Native installers (.deb, .rpm)
