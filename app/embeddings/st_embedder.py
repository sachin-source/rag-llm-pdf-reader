# app/embeddings/st_embedder.py
from typing import List
from sentence_transformers import SentenceTransformer

from app.embeddings.embedder import Embedder


class SentenceTransformerEmbedder(Embedder):
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False,
        ).tolist()

    def embed_query(self, text: str) -> List[float]:
        return self.model.encode(
            text,
            normalize_embeddings=True,
            show_progress_bar=False,
        ).tolist()
