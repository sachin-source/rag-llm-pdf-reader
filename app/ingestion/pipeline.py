from app.ingestion.base import Ingestor


class IngestionPipeline:
    def __init__(self, ingestor: Ingestor):
        self.ingestor = ingestor

    def run(self, source: str) -> str:
        """
        Executes the ingestion pipeline.

        For now:
        source -> raw text

        Later this will expand to:
        source -> raw text -> chunks -> embeddings -> storage
        """
        text = self.ingestor.load(source)

        if not text or not text.strip():
            raise ValueError("No text extracted from source")

        return text
