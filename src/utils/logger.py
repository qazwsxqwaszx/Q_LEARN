"""Logging utilities for the application."""
from __future__ import annotations

import logging
import os
from typing import Optional

from .config_loader import load_config


def setup_logger(config_path: str = "config.yaml") -> logging.Logger:
    """Configure and return the application logger.

    Parameters
    ----------
    config_path:
        Path to the YAML configuration file containing a ``logging`` section.
        Defaults to ``config.yaml``.

    Returns
    -------
    logging.Logger
        Configured root logger instance.
    """
    config = {}
    try:
        config = load_config(config_path)
    except FileNotFoundError:
        pass  # Use defaults if config file missing
    logging_cfg = config.get("logging", {})

    level_name = logging_cfg.get("level", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    log_file = logging_cfg.get("file")
    log_format = logging_cfg.get(
        "format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    logging_kwargs: dict[str, Optional[str]] = {
        "level": level,
        "format": log_format,
    }
    if log_file:
        os.makedirs(os.path.dirname(log_file) or ".", exist_ok=True)
        logging_kwargs["filename"] = log_file

    logging.basicConfig(**logging_kwargs)
    return logging.getLogger("quantum_mechanics")
