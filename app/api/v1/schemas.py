# app/api/v1/schemas.py
from pydantic import BaseModel


class IngestRequest(BaseModel):
    path: str


class IngestResponse(BaseModel):
    chunk_count: int
    embedding_dim: int

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5

class QueryResponse(BaseModel):
    contexts: list[str]
