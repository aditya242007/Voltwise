"""Tests for the forecast API."""

from fastapi.testclient import TestClient

from api.main import app


def test_health_endpoint():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_forecast_reports_missing_model():
    response = TestClient(app).post("/forecast", json={"horizon": 24})
    assert response.status_code == 503