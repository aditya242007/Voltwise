"""Request and response schemas for the forecast API."""

from pydantic import BaseModel, Field


class ForecastRequest(BaseModel):
    """Input for a forecast request."""

    horizon: int = Field(default=24, gt=0)


class ForecastResponse(BaseModel):
    """Forecast values returned by the API."""

    predictions: list[float]