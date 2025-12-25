from fastapi import FastAPI

from app.api.v1.routes import router
from app.embeddings.st_embedder import SentenceTransformerEmbedder

app = FastAPI()


@app.on_event("startup")
def startup_event():
    # Load once at startup
    embedder = SentenceTransformerEmbedder()
    embedder.embed_query(["startup warmup"])

    app.state.embedder = embedder


app.include_router(router, prefix="/api/v1")
