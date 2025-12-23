# LLM RAG Service

A production-oriented, open-source **Retrieval-Augmented Generation (RAG) microservice** built in Python.

The goal of this project is to provide a **clean, extensible, and deployable** backend service that:
- Ingests documents (PDF initially)
- Stores semantic embeddings in a vector database
- Answers user questions strictly using retrieved context

This project is designed with **long-term extensibility** in mind, not as a demo or notebook-based prototype.

---

## 🎯 Scope (Current)

- Upload or read PDF files from a local path
- Extract and chunk text
- Generate embeddings using open-source models
- Store and retrieve embeddings from a vector database
- Answer questions using retrieved context only (RAG)

---

## 🚧 Out of Scope (For Now)

- Web crawling / link ingestion
- UI / frontend
- Authentication / multi-tenancy
- GPU-based inference
- Cloud deployment

These features are intentionally deferred but **architecturally supported**.

---

## 🧠 Design Principles

- Open-source tools only
- Modular, interface-driven architecture
- Replaceable components (LLM, vector DB, embeddings)
- Production-first (Docker, metrics, benchmarks)
- No framework-heavy abstractions (no LangChain)

---

## 🛠 Tech Stack (Initial)

- Python 3.11
- FastAPI
- UV (dependency management)
- Qdrant (vector database)
- Sentence-Transformers (embeddings)
- Docker (local & prod parity)

---

## ▶️ Running Locally (Development)

```bash
uvicorn app.main:app --reload
```

## Health check
```bash
GET /health
```