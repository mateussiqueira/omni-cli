"""Core configuration for Omni CLI."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import toml
import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class OmniConfig(BaseSettings):
    """Global configuration for Omni CLI."""

    model_config = SettingsConfigDict(
        env_prefix="OMNI_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Hostinger
    hostinger_api_token: str = Field(default="", description="Hostinger API token")

    # GitHub
    github_token: str = Field(default="", description="GitHub personal access token")
    github_username: str = Field(default="", description="GitHub username")

    # Unleash
    unleash_url: str = Field(default="", description="Unleash server URL")
    unleash_api_token: str = Field(default="", description="Unleash API token")

    # MCP
    mcp_config_path: str = Field(
        default="~/.config/mcp/servers.json",
        description="Path to MCP servers configuration",
    )

    # Memory
    thunderbolt_disk: str = Field(
        default="/Volumes/ThunderboltSSD",
        description="Path to Thunderbolt SSD",
    )

    @property
    def config_dir(self) -> Path:
        """Return the Omni CLI configuration directory."""
        path = Path.home() / ".config" / "omni"
        path.mkdir(parents=True, exist_ok=True)
        return path

    @property
    def config_file(self) -> Path:
        """Return the Omni CLI configuration file path."""
        return self.config_dir / "config.toml"

    def load_from_file(self) -> None:
        """Load configuration from config file."""
        if not self.config_file.exists():
            return

        try:
            data = toml.load(self.config_file)
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        except Exception as e:
            print(f"⚠️  Error loading config file: {e}")

    def save_to_file(self) -> None:
        """Save current configuration to config file."""
        data = self.model_dump(exclude={"config_dir", "config_file"})
        with open(self.config_file, "w", encoding="utf-8") as f:
            toml.dump(data, f)

    def to_dict(self) -> dict[str, Any]:
        """Return configuration as dictionary."""
        return self.model_dump(exclude={"config_dir", "config_file"})


# Global config instance
config = OmniConfig()
config.load_from_file()
