"""Configuration loading utilities."""
from __future__ import annotations

import os
from typing import Any, Dict

import yaml


def load_config(path: str) -> Dict[str, Any]:
    """Load a YAML configuration file.

    Parameters
    ----------
    path:
        Path to the YAML configuration file.

    Returns
    -------
    Dict[str, Any]
        Parsed configuration as a dictionary.

    Raises
    ------
    FileNotFoundError
        If the configuration file does not exist.
    yaml.YAMLError
        If the YAML file contains invalid syntax.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file '{path}' not found.")
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}
