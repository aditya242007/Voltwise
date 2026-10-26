# Voltwise Product Requirements

## Objective

Explore electricity demand, generate short-term load forecasts, and compare
model performance in a repeatable workflow.

## Users

- Energy analysts exploring historical demand and seasonality.
- Operations teams reviewing near-term forecasts.
- Data scientists comparing forecasting approaches.

## Initial Scope

- Load and validate timestamped electricity demand data.
- Explore demand patterns and calendar effects.
- Build lag, rolling, and calendar features.
- Train, forecast, and evaluate candidate models with time-ordered data.
- Present demand, forecasts, comparisons, and metrics in a dashboard.
- Expose a small HTTP API for forecast requests.

## Success Measures

- Data problems produce actionable validation messages.
- Forecasts and metrics are reproducible from configured inputs.
- Views identify units, time ranges, and model versions.

## Open Decisions

- Select the initial dataset, units, timezone, and forecast horizon.
- Define baselines, evaluation windows, and acceptable metrics.
- Choose artifact storage and API authentication requirements.