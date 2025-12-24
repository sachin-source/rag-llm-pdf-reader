# app/api/v1/routes.py
from fastapi import APIRouter
from app.api.v1.schemas import IngestRequest, IngestResponse
from app.ingestion.local_file import LocalFileIngestor
from app.ingestion.pipeline import IngestionPipeline

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest(request: IngestRequest):
    pipeline = IngestionPipeline(LocalFileIngestor())
    chunks = pipeline.run(request.path)

    return IngestResponse(chunk_count=len(chunks))
