"""Configuration profile management for Omni CLI."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import toml

from omni.core.config import config


def get_profiles_dir() -> Path:
    """Return the directory where profiles are stored."""
    profiles_dir = config.config_dir / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    return profiles_dir


def get_active_profile_file() -> Path:
    """Return the file that stores the active profile name."""
    return config.config_dir / "active_profile"


def get_profile_path(name: str) -> Path:
    """Return the path to a profile file."""
    return get_profiles_dir() / f"{name}.toml"


def list_profiles() -> list[str]:
    """List all available profile names."""
    profiles_dir = get_profiles_dir()
    if not profiles_dir.exists():
        return []
    return sorted([p.stem for p in profiles_dir.glob("*.toml")])


def create_profile(name: str, base_profile: str | None = None) -> None:
    """Create a new configuration profile."""
    profile_path = get_profile_path(name)

    if profile_path.exists():
        raise ValueError(f"Profile '{name}' already exists")

    if base_profile:
        base_path = get_profile_path(base_profile)
        if not base_path.exists():
            raise ValueError(f"Base profile '{base_profile}' does not exist")
        shutil.copy(base_path, profile_path)
    else:
        # Create from current config
        data = config.to_dict()
        with open(profile_path, "w", encoding="utf-8") as f:
            toml.dump(data, f)


def delete_profile(name: str) -> None:
    """Delete a configuration profile."""
    profile_path = get_profile_path(name)

    if not profile_path.exists():
        raise ValueError(f"Profile '{name}' does not exist")

    profile_path.unlink()


def get_active_profile() -> str | None:
    """Get the name of the active profile."""
    active_file = get_active_profile_file()
    if not active_file.exists():
        return None
    return active_file.read_text().strip()


def set_active_profile(name: str | None) -> None:
    """Set the active profile."""
    active_file = get_active_profile_file()

    if name is None:
        if active_file.exists():
            active_file.unlink()
        return

    profile_path = get_profile_path(name)
    if not profile_path.exists():
        raise ValueError(f"Profile '{name}' does not exist")

    active_file.write_text(name)


def load_profile(name: str) -> dict[str, Any]:
    """Load a profile's configuration data."""
    profile_path = get_profile_path(name)
    if not profile_path.exists():
        raise ValueError(f"Profile '{name}' does not exist")
    return toml.load(profile_path)


def load_active_profile() -> dict[str, Any] | None:
    """Load the active profile's configuration data."""
    active = get_active_profile()
    if not active:
        return None
    return load_profile(active)


def apply_profile(name: str) -> None:
    """Apply a profile to the current configuration."""
    data = load_profile(name)
    for key, value in data.items():
        if hasattr(config, key):
            setattr(config, key, value)
    config.save_to_file()
    set_active_profile(name)


def initialize_config_with_profile() -> None:
    """Initialize config with active profile if set."""
    active = get_active_profile()
    if active:
        try:
            data = load_profile(active)
            for key, value in data.items():
                if hasattr(config, key):
                    setattr(config, key, value)
        except Exception:
            pass
