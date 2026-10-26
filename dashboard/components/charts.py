"""Reusable Plotly charts for the Voltwise dashboard."""

import plotly.express as px


def demand_chart(frame, x="timestamp", y="demand"):
    """Create a demand time-series figure."""
    return px.line(frame, x=x, y=y, title="Electricity demand")