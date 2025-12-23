from fastapi import APIRouter

from app.api.v1.schemas import IngestRequest, IngestResponse
from app.ingestion.local_text import LocalTextIngestor
from app.ingestion.pipeline import IngestionPipeline

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/ingest", response_model=IngestResponse)
def ingest_file(request: IngestRequest):
    ingestor = LocalTextIngestor()
    pipeline = IngestionPipeline(ingestor)

    text = pipeline.run(request.path)

    return IngestResponse(characters=len(text))
