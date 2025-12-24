# app/embeddings/embedder.py
from abc import ABC, abstractmethod
from typing import List


class Embedder(ABC):
    """Contract for embedding models."""

    @abstractmethod
    def embed(self, texts: List[str]) -> List[list[float]]:
        pass
