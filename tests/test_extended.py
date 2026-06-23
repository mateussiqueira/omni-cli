"""Extended tests for Omni CLI."""

from __future__ import annotations

import json
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import httpx
import typer
from typer.testing import CliRunner

from omni.cli import app
from omni.core.config import config
from omni.core.executor import run_command
from omni.core.logger import audit_command, setup_audit_logging, setup_logging
from omni.core.plugins import discover_plugins, list_plugins, register_plugins
from omni.core.profiles import (
    apply_profile,
    create_profile,
    delete_profile,
    get_active_profile,
    list_profiles,
)

runner = CliRunner()


def test_plugins_list() -> None:
    """Test plugins list command."""
    result = runner.invoke(app, ["plugins", "list"])
    assert result.exit_code == 0
    assert "No plugins installed" in result.output or "Omni CLI Plugins" in result.output


def test_update_check() -> None:
    """Test update check command."""
    with patch("httpx.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"info": {"version": "0.1.0"}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = runner.invoke(app, ["update", "--check"])
        assert result.exit_code == 0
        assert "already up to date" in result.output


def test_config_profile_create_list() -> None:
    """Test config profile create and list."""
    from omni.core.profiles import get_profiles_dir

    # Clean up
    profiles_dir = get_profiles_dir()
    for p in profiles_dir.glob("*.toml"):
        p.unlink()
    active_file = config.config_dir / "active_profile"
    if active_file.exists():
        active_file.unlink()

    result = runner.invoke(app, ["config", "profile", "create", "test-profile"])
    assert result.exit_code == 0
    assert "created" in result.output

    result = runner.invoke(app, ["config", "profile", "list"])
    assert result.exit_code == 0
    assert "test-profile" in result.output

    # Cleanup
    runner.invoke(app, ["config", "profile", "delete", "test-profile", "--force"])


def test_config_profile_use() -> None:
    """Test config profile use command."""
    runner.invoke(app, ["config", "profile", "create", "use-test"])

    result = runner.invoke(app, ["config", "profile", "use", "use-test"])
    assert result.exit_code == 0
    assert "Active profile set" in result.output

    # Cleanup
    runner.invoke(app, ["config", "profile", "delete", "use-test", "--force"])


def test_cloudflare_missing_token() -> None:
    """Test cloudflare command with missing token."""
    original = config.cloudflare_api_token
    config.cloudflare_api_token = ""

    result = runner.invoke(app, ["cloudflare", "zones"])
    assert result.exit_code == 1
    assert "Cloudflare API token not configured" in result.output

    config.cloudflare_api_token = original


def test_vercel_missing_token() -> None:
    """Test vercel command with missing token."""
    original = config.vercel_token
    config.vercel_token = ""

    result = runner.invoke(app, ["vercel", "projects"])
    assert result.exit_code == 1
    assert "Vercel token not configured" in result.output

    config.vercel_token = original


def test_aws_status_no_cli() -> None:
    """Test aws status command when AWS CLI is not available."""
    with patch("omni.commands.aws.run_command") as mock_run:
        mock_run.return_value = MagicMock(success=False, stdout="", stderr="")
        result = runner.invoke(app, ["aws", "status"])
        assert result.exit_code == 1
        assert "AWS CLI is not installed" in result.output


def test_logger_setup() -> None:
    """Test logging setup."""
    logger = setup_logging("INFO")
    assert logger is not None
    assert logger.level == 20  # INFO level


def test_audit_logging() -> None:
    """Test audit logging."""
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        log_path = f.name

    try:
        os.environ["OMNI_AUDIT_LOG"] = log_path
        audit_command(["omni", "test"])

        with open(log_path, "r") as f:
            content = f.read()
        assert "omni test" in content
    finally:
        del os.environ["OMNI_AUDIT_LOG"]
        if os.path.exists(log_path):
            os.unlink(log_path)


def test_executor_success() -> None:
    """Test command executor with successful command."""
    result = run_command(["echo", "hello"])
    assert result.success
    assert "hello" in result.stdout


def test_executor_failure() -> None:
    """Test command executor with failing command."""
    result = run_command(["false"])
    assert not result.success
    assert result.returncode == 1


def test_executor_not_found() -> None:
    """Test command executor with missing command."""
    result = run_command(["nonexistent_command_xyz"])
    assert not result.success
    assert result.returncode == -1


def test_discover_plugins() -> None:
    """Test plugin discovery returns dict."""
    plugins = discover_plugins()
    assert isinstance(plugins, dict)


def test_list_plugins() -> None:
    """Test list_plugins returns list."""
    plugins = list_plugins()
    assert isinstance(plugins, list)


def test_profile_module() -> None:
    """Test profile module functions."""
    from omni.core.profiles import get_profiles_dir

    # Clean state
    profiles_dir = get_profiles_dir()
    for p in profiles_dir.glob("*.toml"):
        p.unlink()
    active_file = config.config_dir / "active_profile"
    if active_file.exists():
        active_file.unlink()

    # Create profile
    create_profile("module-test")
    assert "module-test" in list_profiles()

    # Apply profile
    apply_profile("module-test")
    assert get_active_profile() == "module-test"

    # Delete profile
    delete_profile("module-test")
    assert "module-test" not in list_profiles()
