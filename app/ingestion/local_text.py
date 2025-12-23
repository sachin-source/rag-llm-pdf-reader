from pathlib import Path
from app.ingestion.base import Ingestor


class LocalTextIngestor(Ingestor):
    """
    Temporary ingestor for local .txt files.
    PDF ingestor will replace this later.
    """

    def load(self, source: str) -> str:
        path = Path(source)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {source}")

        if not path.is_file():
            raise ValueError(f"Not a file: {source}")

        return path.read_text(encoding="utf-8")
