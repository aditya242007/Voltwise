# Voltwise
Predict smarter. Power better.

Voltwise is a starter project for exploring electricity demand and building
load forecasts with a Streamlit dashboard and reusable Python pipeline.

## Setup

Use Python 3.10 or newer. Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, place source datasets under `data/raw/`, and
start the dashboard with `streamlit run app.py`. See [PRD.md](PRD.md) for
product scope and [data/README.md](data/README.md) for dataset guidance.

This repository is an initial scaffold; data ingestion, modeling, API, and
dashboard workflows need to be adapted to a selected dataset and deployment.
