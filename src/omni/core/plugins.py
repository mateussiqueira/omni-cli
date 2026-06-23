"""Plugin discovery and loading for Omni CLI."""

from __future__ import annotations

import importlib.metadata
import logging
from typing import Any

import typer

logger = logging.getLogger(__name__)

PLUGIN_GROUP = "omni.plugins"


def discover_plugins() -> dict[str, typer.Typer]:
    """Discover installed Omni CLI plugins via entry points."""
    plugins: dict[str, typer.Typer] = {}

    try:
        entry_points = importlib.metadata.entry_points()
        # importlib.metadata.entry_points() behavior differs between Python versions
        if hasattr(entry_points, "select"):
            plugin_entries = entry_points.select(group=PLUGIN_GROUP)
        else:
            plugin_entries = entry_points.get(PLUGIN_GROUP, [])
    except Exception as e:
        logger.warning(f"Failed to discover plugins: {e}")
        return plugins

    for entry in plugin_entries:
        try:
            app = entry.load()
            if isinstance(app, typer.Typer):
                plugins[entry.name] = app
                logger.debug(f"Loaded plugin: {entry.name}")
            else:
                logger.warning(f"Plugin {entry.name} does not expose a Typer app")
        except Exception as e:
            logger.warning(f"Failed to load plugin {entry.name}: {e}")

    return plugins


def register_plugins(app: typer.Typer) -> None:
    """Register discovered plugins with the main Omni CLI app."""
    plugins = discover_plugins()

    for name, plugin_app in plugins.items():
        try:
            app.add_typer(plugin_app, name=name, help=f"🔌 {name} plugin")
            logger.debug(f"Registered plugin command: {name}")
        except Exception as e:
            logger.warning(f"Failed to register plugin {name}: {e}")


def list_plugins() -> list[dict[str, Any]]:
    """Return a list of discovered plugins with metadata."""
    plugins = []

    try:
        entry_points = importlib.metadata.entry_points()
        if hasattr(entry_points, "select"):
            plugin_entries = entry_points.select(group=PLUGIN_GROUP)
        else:
            plugin_entries = entry_points.get(PLUGIN_GROUP, [])
    except Exception:
        return plugins

    for entry in plugin_entries:
        try:
            dist = entry.dist
            metadata = {
                "name": entry.name,
                "module": entry.value,
                "package": dist.name if dist else "unknown",
                "version": dist.version if dist else "unknown",
            }
            plugins.append(metadata)
        except Exception as e:
            plugins.append({"name": entry.name, "error": str(e)})

    return plugins
