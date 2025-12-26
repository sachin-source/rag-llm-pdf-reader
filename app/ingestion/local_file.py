# app/ingestion/local_file.py
from pathlib import Path
from app.ingestion.ingestor import Ingestor
import pdfplumber


class LocalFileIngestor(Ingestor):
    def load(self, source: str) -> str:
        path = Path(source)

        if not path.exists() or not path.is_file():
            raise FileNotFoundError(f"Invalid file path: {source}")

        if path.suffix.lower() == ".pdf":
            text = ""
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text

        return path.read_text(encoding="utf-8")
