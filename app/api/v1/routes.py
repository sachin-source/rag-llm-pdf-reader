from fastapi import APIRouter, Request

from app.api.v1.schemas import IngestRequest, IngestResponse
from app.ingestion.local_file import LocalFileIngestor
from app.ingestion.pipeline import IngestionPipeline

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest(request: IngestRequest, http_request: Request):
    embedder = http_request.app.state.embedder

    pipeline = IngestionPipeline(
        ingestor=LocalFileIngestor(),
        embedder=embedder,
    )

    results = pipeline.run(request.path)

    return IngestResponse(
        chunk_count=len(results),
        embedding_dim=len(results[0][1]),
    )
