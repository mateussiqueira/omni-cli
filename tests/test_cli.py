"""Basic tests for Omni CLI."""

from typer.testing import CliRunner

from omni.cli import app

runner = CliRunner()


def test_version() -> None:
    """Test version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "Omni CLI" in result.output


def test_status() -> None:
    """Test status command."""
    result = runner.invoke(app, ["status"])
    assert result.exit_code == 0
    assert "ready to use" in result.output


def test_config_show() -> None:
    """Test config show command."""
    result = runner.invoke(app, ["config", "show"])
    assert result.exit_code == 0
    assert "Configuration" in result.output


def test_memory_status() -> None:
    """Test memory status command."""
    result = runner.invoke(app, ["memory", "status"])
    assert result.exit_code == 0
    assert "Memory Status" in result.output
