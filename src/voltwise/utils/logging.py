"""Application logging configuration."""

import logging


def configure_logging(level: str = "INFO") -> None:
    """Configure a consistent application-wide logging format."""
    logging.basicConfig(level=level.upper(), format="%(asctime)s %(levelname)s %(name)s: %(message)s")