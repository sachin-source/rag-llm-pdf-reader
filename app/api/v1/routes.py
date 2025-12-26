from fastapi import APIRouter, Request

from app.api.v1.schemas import IngestRequest, IngestResponse
from app.ingestion.local_file import LocalFileIngestor
from app.ingestion.pipeline import IngestionPipeline

from app.retrieval.service import RetrievalService
from app.vectorstore.qdrant import QdrantVectorStore
from app.api.v1.schemas import QueryRequest, QueryResponse

from app.llm.llama_cpp import LlamaCppLLM
from app.qa.service import QAService

router = APIRouter()

llm = LlamaCppLLM(
    model_path="model/mistral.gguf",
)

qa_service = QAService(llm)

@router.post("/ingest", response_model=IngestResponse)
def ingest(request: IngestRequest, http_request: Request):
    embedder = http_request.app.state.embedder

    pipeline = IngestionPipeline(
        ingestor=LocalFileIngestor(),
        embedder=embedder,
        vector_store=QdrantVectorStore(),
    )

    results = pipeline.run(request.path)

    return IngestResponse(
        chunk_count=len(results),
        embedding_dim=len(results[0][1]),
    )

@router.post("/query", response_model=QueryResponse)
def query(
    request: QueryRequest,
    http_request: Request,
):
    embedder = http_request.app.state.embedder
    vector_store = QdrantVectorStore()

    service = RetrievalService(
        embedder=embedder,
        vector_store=vector_store,
    )

    contexts = service.retrieve(
        question=request.question,
        top_k=request.top_k,
    )
    
    answer = qa_service.answer(
    question=request.question,
    contexts=contexts,
)

    return {
        "question": request.question,
        "answer": answer,
        "contexts": contexts,
    }

    # return QueryResponse(contexts=contexts)
