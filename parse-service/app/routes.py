import hmac
import os

from fastapi import APIRouter, Header, HTTPException

from .models import ParseRequest

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy", "service": "parse-service"}


@router.post("/parse")
def parse_invoice(
    _: ParseRequest,
    parser_api_key: str | None = Header(default=None, alias="X-Parser-Api-Key"),
) -> None:
    expected_key = os.getenv("PARSER_API_KEY")
    if not expected_key:
        raise HTTPException(status_code=503, detail="parser authentication is not configured")
    if not parser_api_key or not hmac.compare_digest(parser_api_key, expected_key):
        raise HTTPException(status_code=401, detail="invalid parser credentials")
    raise HTTPException(status_code=501, detail="parser not implemented")
