"""Load electricity demand data from local sources."""

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset into a DataFrame."""
    return pd.read_csv(path)