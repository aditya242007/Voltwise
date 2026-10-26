"""Feature construction for time-series demand data."""

import pandas as pd


def build_features(frame: pd.DataFrame, timestamp_column: str = "timestamp", target_column: str = "demand") -> pd.DataFrame:
    """Return a copy with basic calendar, lag, and rolling features."""
    result = frame.copy()
    timestamps = pd.to_datetime(result[timestamp_column])
    result["hour"] = timestamps.dt.hour
    result["day_of_week"] = timestamps.dt.dayofweek
    result["month"] = timestamps.dt.month
    result[f"{target_column}_lag_1"] = result[target_column].shift(1)
    result[f"{target_column}_rolling_mean_24"] = result[target_column].shift(1).rolling(24).mean()
    return result