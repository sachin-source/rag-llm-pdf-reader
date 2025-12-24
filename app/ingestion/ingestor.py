# app/ingestion/ingestor.py
from abc import ABC, abstractmethod


class Ingestor(ABC):
    """Contract for all ingestion sources."""

    @abstractmethod
    def load(self, source: str) -> str:
        """Return raw extracted text."""
        pass
