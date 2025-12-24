# app/api/v1/routes.py
from fastapi import APIRouter

from app.api.v1.schemas import IngestRequest, IngestResponse
from app.ingestion.local_file import LocalFileIngestor
from app.ingestion.pipeline import IngestionPipeline
from app.embeddings.st_embedder import SentenceTransformerEmbedder

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest(request: IngestRequest):
    pipeline = IngestionPipeline(
        ingestor=LocalFileIngestor(),
        embedder=SentenceTransformerEmbedder(),
    )

    results = pipeline.run(request.path)

    return IngestResponse(
        chunk_count=len(results),
        embedding_dim=len(results[0][1]),
    )
