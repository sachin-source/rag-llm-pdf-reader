# app/api/v1/schemas.py
from pydantic import BaseModel


class IngestRequest(BaseModel):
    path: str


class IngestResponse(BaseModel):
    chunk_count: int
