"""Candidate model training entry point."""


def train_model(features, target, model=None):
    """Fit a supplied scikit-learn-compatible estimator."""
    if model is None:
        raise ValueError("Provide a model estimator to train")
    return model.fit(features, target)