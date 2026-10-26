"""Tests for time-series feature construction."""

import pandas as pd

from voltwise.features.build_features import build_features


def test_build_features_adds_calendar_and_lag_columns():
    frame = pd.DataFrame(
        {"timestamp": pd.date_range("2025-01-01", periods=3, freq="h"), "demand": [1, 2, 3]}
    )
    result = build_features(frame)
    assert {"hour", "day_of_week", "month", "demand_lag_1", "demand_rolling_mean_24"} <= set(result)
    assert pd.isna(result.loc[0, "demand_lag_1"])