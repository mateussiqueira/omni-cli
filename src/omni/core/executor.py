"""Command executor utilities for Omni CLI."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class CommandResult:
    """Result of a command execution."""

    returncode: int
    stdout: str
    stderr: str
    command: str

    @property
    def success(self) -> bool:
        """Check if command was successful."""
        return self.returncode == 0


def run_command(
    command: list[str] | str,
    cwd: str | Path | None = None,
    env: dict[str, str] | None = None,
    shell: bool = False,
    check: bool = False,
    timeout: int | None = 60,
) -> CommandResult:
    """Run a shell command and return the result."""
    if isinstance(command, str) and not shell:
        command = command.split()

    merged_env = dict(os.environ) if env else None
    if env and merged_env:
        merged_env.update(env)

    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=merged_env,
            shell=shell,
            check=check,
            timeout=timeout,
            capture_output=True,
            text=True,
        )
        return CommandResult(
            returncode=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
            command=str(command),
        )
    except subprocess.TimeoutExpired as e:
        return CommandResult(
            returncode=-1,
            stdout=e.stdout or "",
            stderr=e.stderr or "",
            command=str(command),
        )
    except FileNotFoundError:
        return CommandResult(
            returncode=-1,
            stdout="",
            stderr=f"Command not found: {command}",
            command=str(command),
        )
