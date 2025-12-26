from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct, SearchParams
import uuid

from app.vectorstore.base import VectorStore


class QdrantVectorStore(VectorStore):
    def __init__(
        self,
        collection_name: str = "documents",
        vector_size: int = 384,
        host: str = "localhost",
        port: int = 6333,
    ):
        self.collection_name = collection_name
        self.client = QdrantClient(host=host, port=port)
        self._ensure_collection(vector_size)

    def _ensure_collection(self, vector_size: int) -> None:
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )

    def add(
        self,
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
    ):
        points = []

        for text, vector, metadata in zip(texts, embeddings, metadatas):
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={
                        "text": text,
                        **metadata,
                    },
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(self, query_vector: list[float], limit: int = 5):
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
            with_payload=True,
            with_vectors=True,
            score_threshold=0.0,
        )
        return results
