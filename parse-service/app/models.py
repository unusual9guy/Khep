from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, field_validator


class ParseRequest(BaseModel):
    pdf_url: AnyHttpUrl
    upload_timestamp: datetime

    @field_validator("pdf_url")
    @classmethod
    def require_https(cls, value: AnyHttpUrl) -> AnyHttpUrl:
        if value.scheme != "https":
            raise ValueError("pdf_url must use HTTPS")
        return value
