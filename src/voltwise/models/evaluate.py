"""Forecast evaluation helpers."""

from sklearn.metrics import mean_absolute_error, mean_squared_error


def evaluate(y_true, y_pred) -> dict[str, float]:
    """Return common regression metrics."""
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(mean_squared_error(y_true, y_pred) ** 0.5),
    }