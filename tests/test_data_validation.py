"""Tests for demand data validation."""

import pandas as pd
import pytest

from voltwise.data.validate_data import validate_demand_data


def test_validate_demand_data_accepts_sorted_numeric_data():
    frame = pd.DataFrame(
        {"timestamp": ["2025-01-01 00:00", "2025-01-01 01:00"], "demand": [1.0, 2.0]}
    )
    validate_demand_data(frame)


def test_validate_demand_data_rejects_missing_columns():
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_demand_data(pd.DataFrame({"timestamp": ["2025-01-01"]}))