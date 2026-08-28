import os

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

os.environ["PARSER_API_KEY"] = "test-parser-key"

from app.main import app
from app.models import ParseRequest

client = TestClient(app)


def test_health_returns_service_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "parse-service",
    }


def test_parse_placeholder_returns_not_implemented() -> None:
    response = client.post(
        "/parse",
        json={
            "pdf_url": "https://storage.example.test/invoice.pdf",
            "upload_timestamp": "2026-08-28T12:00:00Z",
        },
        headers={"X-Parser-Api-Key": "test-parser-key"},
    )

    assert response.status_code == 501
    assert response.json() == {"detail": "parser not implemented"}


def test_parse_requires_api_key() -> None:
    response = client.post(
        "/parse",
        json={
            "pdf_url": "https://storage.example.test/invoice.pdf",
            "upload_timestamp": "2026-08-28T12:00:00Z",
        },
    )

    assert response.status_code == 401


def test_parse_request_rejects_insecure_pdf_urls() -> None:
    with pytest.raises(ValidationError):
        ParseRequest(
            pdf_url="http://storage.example.test/invoice.pdf",
            upload_timestamp="2026-08-28T12:00:00Z",
        )
