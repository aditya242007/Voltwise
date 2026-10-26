"""Forecast generation helpers."""


def predict(model, features):
    """Generate predictions using a fitted estimator."""
    return model.predict(features)