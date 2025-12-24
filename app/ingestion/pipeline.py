# app/ingestion/pipeline.py
from typing import List
from app.ingestion.ingestor import Ingestor
from app.processing.chunker import chunk_text, TextChunk


class IngestionPipeline:
    def __init__(
        self,
        ingestor: Ingestor,
        chunk_size: int = 500,
        overlap: int = 100,
    ):
        self.ingestor = ingestor
        self.chunk_size = chunk_size
        self.overlap = overlap

    def run(self, source: str) -> List[TextChunk]:
        raw_text = self.ingestor.load(source)

        if not raw_text.strip():
            raise ValueError("Empty content extracted")

        return chunk_text(
            raw_text,
            chunk_size=self.chunk_size,
            overlap=self.overlap,
        )
