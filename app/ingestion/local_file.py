# app/ingestion/local_file.py
from pathlib import Path
from app.ingestion.ingestor import Ingestor


class LocalFileIngestor(Ingestor):
    def load(self, source: str) -> str:
        path = Path(source)

        if not path.exists() or not path.is_file():
            raise FileNotFoundError(f"Invalid file path: {source}")

        return path.read_text(encoding="utf-8")
