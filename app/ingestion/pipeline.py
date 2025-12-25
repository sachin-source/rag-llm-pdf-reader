# app/ingestion/pipeline.py
from typing import List, Tuple

from app.ingestion.ingestor import Ingestor
from app.processing.chunker import chunk_text, TextChunk
from app.embeddings.embedder import Embedder


class IngestionPipeline:
    def __init__(
        self,
        ingestor: Ingestor,
        embedder: Embedder,
        chunk_size: int = 500,
        overlap: int = 100,
    ):
        self.ingestor = ingestor
        self.embedder = embedder
        self.chunk_size = chunk_size
        self.overlap = overlap

    def run(self, source: str) -> List[Tuple[TextChunk, list[float]]]:
        raw_text = self.ingestor.load(source)

        if not raw_text.strip():
            raise ValueError("Empty content extracted")

        chunks = chunk_text(
            raw_text,
            chunk_size=self.chunk_size,
            overlap=self.overlap,
        )

        texts = [chunk.text for chunk in chunks]
        vectors = self.embedder.embed_query(texts)

        return list(zip(chunks, vectors))
