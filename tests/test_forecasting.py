"""Tests for forecasting workflow orchestration."""

import pandas as pd

from voltwise.pipelines.forecasting import prepare_forecasting_data


def test_prepare_forecasting_data_validates_and_builds_features():
    frame = pd.DataFrame(
        {"timestamp": pd.date_range("2025-01-01", periods=2, freq="h"), "demand": [1.0, 2.0]}
    )
    result = prepare_forecasting_data(frame)
    assert "hour" in result