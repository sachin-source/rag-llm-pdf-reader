from typing import List

from app.embeddings.embedder import Embedder
from app.vectorstore.base import VectorStore

class RetrievalService:
    def __init__(self, vector_store:VectorStore, embedder:Embedder):
        self.vector_store = vector_store
        self.embedder = embedder

    def retrieve(self, question: str, top_k: int = 5) -> list[str]:
        query_vector = self.embedder.embed_query(question)

        points_response = self.vector_store.search(
            query_vector=query_vector,
            limit=top_k
        )
        
        if hasattr(points_response, "points"):
            points = points_response.points
        elif isinstance(points_response, dict) and "result" in points_response:
            points = points_response["result"]
        else:
            points = points_response
        
        contexts = []

        for p in points:
            if hasattr(p, "payload") and "text" in p.payload:
                contexts.append(p.payload["text"])

        return contexts

        
        # print(results)
        # print(type(results[0]), len(results[0]))

        # contexts = [ p.payload["text"] for p in points if p.payload and "text" in p.payload]

        # return contexts

# class RetrievalService:
#     def __init__(
#         self,
#         embedder: Embedder,
#         vector_store: VectorStore,
#     ):
#         self.embedder = embedder
#         self.vector_store = vector_store

#     def retrieve(self, question: str, top_k: int) -> List[str]:
#         query_vector = self.embedder.embed([question])[0]

#         results = self.vector_store.search(
#             query_vector=query_vector,
#             limit=top_k,
#         )

#         return [
#             hit.payload["text"]
#             for hit in results
#             if "text" in hit.payload
#         ]
