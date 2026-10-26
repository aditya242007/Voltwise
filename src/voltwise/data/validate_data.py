"""Validation helpers for electricity demand data."""

import pandas as pd


def validate_demand_data(frame: pd.DataFrame, timestamp_column: str = "timestamp", target_column: str = "demand") -> None:
    """Raise ValueError when required fields or values are invalid."""
    missing = {timestamp_column, target_column} - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    timestamps = pd.to_datetime(frame[timestamp_column], errors="coerce")
    if timestamps.isna().any():
        raise ValueError(f"{timestamp_column} contains invalid timestamps")
    if not timestamps.is_monotonic_increasing:
        raise ValueError(f"{timestamp_column} must be sorted in ascending order")
    if pd.to_numeric(frame[target_column], errors="coerce").isna().any():
        raise ValueError(f"{target_column} must contain numeric, non-missing values")