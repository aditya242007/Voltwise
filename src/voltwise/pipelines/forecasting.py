"""Reusable forecasting workflow orchestration."""

from voltwise.data.validate_data import validate_demand_data
from voltwise.features.build_features import build_features


def prepare_forecasting_data(frame, timestamp_column="timestamp", target_column="demand"):
    """Validate input and construct features for downstream modeling."""
    validate_demand_data(frame, timestamp_column, target_column)
    return build_features(frame, timestamp_column, target_column)