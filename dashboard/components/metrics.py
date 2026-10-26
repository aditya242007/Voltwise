"""Reusable dashboard metric components."""

import streamlit as st


def show_forecast_metrics(metrics: dict[str, float]) -> None:
    """Render forecast metrics as Streamlit metric columns."""
    columns = st.columns(max(1, len(metrics)))
    for column, (name, value) in zip(columns, metrics.items()):
        column.metric(name.upper(), f"{value:,.3f}")