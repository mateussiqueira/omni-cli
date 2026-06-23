"""Logging and audit utilities for Omni CLI."""

from __future__ import annotations

import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from omni.core.config import config


class AuditFilter(logging.Filter):
    """Filter to identify audit log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        return hasattr(record, "audit") and record.audit


def get_log_directory() -> Path:
    """Return the log directory for Omni CLI."""
    log_dir = Path.home() / ".config" / "omni" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    return log_dir


def setup_logging(log_level: str | None = None) -> logging.Logger:
    """Setup Omni CLI logging based on environment variables."""
    if log_level is None:
        log_level = os.environ.get("OMNI_LOG_LEVEL", "WARNING").upper()

    logger = logging.getLogger("omni")
    logger.setLevel(getattr(logging, log_level, logging.WARNING))

    # Avoid adding multiple handlers
    if logger.handlers:
        return logger

    # Console handler
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler (if log directory is writable)
    try:
        log_dir = get_log_directory()
        file_handler = logging.FileHandler(log_dir / "omni.log")
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    except Exception:
        # If we can't write to log file, continue with console only
        pass

    return logger


def setup_audit_logging(audit_log_path: str | None = None) -> logging.Logger | None:
    """Setup audit logging if OMNI_AUDIT_LOG is set."""
    if audit_log_path is None:
        audit_log_path = os.environ.get("OMNI_AUDIT_LOG")

    if not audit_log_path:
        return None

    audit_logger = logging.getLogger("omni.audit")
    audit_logger.setLevel(logging.INFO)

    # Avoid adding multiple handlers
    if audit_logger.handlers:
        return audit_logger

    try:
        Path(audit_log_path).parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(audit_log_path)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        handler.setFormatter(formatter)
        handler.addFilter(AuditFilter())
        audit_logger.addHandler(handler)
    except Exception:
        return None

    return audit_logger


def audit_command(command: list[str], **kwargs: Any) -> None:
    """Log an executed command to the audit log."""
    audit_logger = setup_audit_logging()
    if not audit_logger:
        return

    user = os.environ.get("USER", "unknown")
    timestamp = datetime.now(timezone.utc).isoformat()
    cmd_str = " ".join(command)
    extra_info = ", ".join(f"{k}={v}" for k, v in kwargs.items())

    record = audit_logger.makeRecord(
        name=audit_logger.name,
        level=logging.INFO,
        fn="",
        lno=0,
        msg=f"user={user} command={cmd_str} {extra_info}",
        args=(),
        exc_info=None,
    )
    setattr(record, "audit", True)
    audit_logger.handle(record)
