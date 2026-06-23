# Plugin Development Guide

Learn how to extend Omni CLI with custom commands.

## Table of Contents

- [Plugin Architecture](#plugin-architecture)
- [Creating a Simple Plugin](#creating-a-simple-plugin)
- [Registering Plugins](#registering-plugins)
- [Accessing Core Utilities](#accessing-core-utilities)
- [Plugin Configuration](#plugin-configuration)
- [Distribution](#distribution)

## Plugin Architecture

Omni CLI uses Typer for command registration. A plugin is simply a Python module that exposes a Typer app.

```text
my_omni_plugin/
├── __init__.py
└── commands.py
```

## Creating a Simple Plugin

Create `my_omni_plugin/commands.py`:

```python
import typer
from rich.console import Console

app = typer.Typer(help="My custom Omni CLI plugin")
console = Console()

@app.command("hello")
def hello(name: str = typer.Option("World", "--name", "-n")) -> None:
    """Say hello from my plugin."""
    console.print(f"[green]Hello, {name}![/green]")

@app.command("status")
def status() -> None:
    """Show plugin status."""
    console.print("[blue]My plugin is running[/blue]")
```

Create `my_omni_plugin/__init__.py`:

```python
from my_omni_plugin.commands import app

__all__ = ["app"]
```

## Registering Plugins

Plugins can be registered via entry points in `pyproject.toml`:

```toml
[project.entry-points."omni.plugins"]
myplugin = "my_omni_plugin:app"
```

Omni CLI will discover and register all plugins automatically.

### Manual registration (for development)

Edit `src/omni/cli.py`:

```python
from my_omni_plugin import app as my_plugin_app

app.add_typer(my_plugin_app, name="myplugin", help="My custom plugin")
```

## Accessing Core Utilities

Plugins can reuse Omni CLI core utilities:

```python
from omni.core.config import config
from omni.core.executor import run_command

# Use configuration
api_token = config.hostinger_api_token

# Run shell commands
result = run_command(["git", "status"])
```

## Plugin Configuration

Plugins can define their own config keys:

```python
# In my_omni_plugin/config_extension.py
from omni.core.config import config

# Access or set custom config
my_setting = config.to_dict().get("myplugin_setting", "default")
```

Users set values via:

```bash
omni config set myplugin_setting value
```

## Distribution

Publish your plugin on PyPI:

```toml
[project]
name = "omni-cli-myplugin"
version = "0.1.0"
dependencies = ["omni-cli>=0.1.0"]

[project.entry-points."omni.plugins"]
myplugin = "my_omni_plugin:app"
```

Users install it with:

```bash
pip install omni-cli-myplugin
```

## Best Practices

- Use Typer for CLI structure
- Use Rich for beautiful output
- Handle errors gracefully
- Add tests for your commands
- Document your plugin commands
- Prefix plugin package names with `omni-cli-`
