"""Project configuration loading."""

from pathlib import Path

import yaml


def load_config(path: str | Path = "configs/config.yaml") -> dict:
    """Load a YAML configuration file as a dictionary."""
    with Path(path).open(encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)
    if not isinstance(config, dict):
        raise ValueError("Configuration must contain a YAML mapping")
    return config