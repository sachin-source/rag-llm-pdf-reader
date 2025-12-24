from abc import ABC, abstractmethod
from typing import List, Any

class VectorStore(ABC):
    @abstractmethod
    def add(self, vectors: List[list[float]], payloads: List[dict], ) -> None:
        pass

    @abstractmethod
    def search(self, query_vector: list[float], limit: int = 5, ) -> List[Any]:
        pass
