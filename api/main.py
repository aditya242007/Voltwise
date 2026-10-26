"""FastAPI application entry point."""

from fastapi import FastAPI, HTTPException

from api.schemas import ForecastRequest, ForecastResponse

app = FastAPI(title="Voltwise Forecast API")


@app.get("/health")
def health() -> dict[str, str]:
    """Report API process health."""
    return {"status": "ok"}


@app.post("/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest) -> ForecastResponse:
    """Return service unavailable until a model is configured."""
    raise HTTPException(status_code=503, detail="No forecasting model is configured")