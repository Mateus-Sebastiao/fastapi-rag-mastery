# FastAPI RAG Mastery: From Naive to Agentic Ecosystem

A production-grade, highly scalable RAG (Retrieval-Augmented Generation) infrastructure built with FastAPI, adhering to clean architecture patterns (**Modules-Service-Repository**). This project serves as a step-by-step masterclass, guiding developers from foundational local RAG systems up to advanced multi-agent orchestrations.

## 🚀 Architecture Highlights
- **Layered Clean Architecture**: Strict separation of concerns using the Module-Service-Repository pattern.
- **100% Local & Privacy-First**: Completely free stack running locally via Ollama, ChromaDB, and HuggingFace.
- **Unified AI Gateway**: Integrated with `litellm` for standardized Open-AI compatible downstream inference calls.

---

## 🛠️ Tech Stack
- **Framework**: FastAPI (Asynchronous engine)
- **ASGI Server**: Uvicorn
- **LLM Engine**: Ollama (Llama 3.2:3b)
- **AI Proxy Gateway**: LiteLLM
- **Vector Database**: ChromaDB
- **Embeddings**: HuggingFace (Sentence-Transformers)

---

## 🔧 Getting Started

### 1. Prerequisites
Ensure you have **Ollama** installed and running locally with the Llama3 model pull:
```bash
ollama pull llama3.2:3b
```

### 2. Environment Setup
Clone the repository and create your configuration file:
```bash
cp .env.example .env
```

Fill in your `.env` variables:
```env
APP_NAME="FastAPI RAG Mastery"
ENVIRONMENT="development"
LITELLM_PROXY_URL="http://localhost:4000"
OLLAMA_API_BASE="http://localhost:11434"
CHROMA_PERSIST_DIR="./chroma_db"
```

### 3. Installation
Install dependencies and run the Uvicorn production server:
```bash
uv sync
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🧭 Roadmap

- [x] **Module 01: Beginner — Naive RAG**
  - Foundational vector pipelines (Retrieval -> Augmentation -> Generation).
  - Raw string payload ingestion & basic token-length splitters.
  - Basic Vector Search using ChromaDB + local HuggingFace embeddings.

- [ ] **Module 02: Intermediate — Advanced Production Retrieval**
  - **Document Parsing Engine**: Multi-format parsing (PDF/Markdown) handling file uploads.
  - **Deterministic Text Splitting**: LangChain's `RecursiveCharacterTextSplitter` with semantic overlap.
  - **Query Rewriting**: LLM-driven expansion of user intent before lookup.
  - **Hybrid Search**: Combining Dense Vectors (ChromaDB) with Sparse Retrieval (BM25 Keyword Matching).
  - **Reranking Cross-Encoders**: Sorting top-K contexts using specialized local scoring models.

- [ ] **Module 03: Advanced — Production Evaluation & Guardrails**
  - **RAG Evaluation (Eval)**: Automated testing framework using `Ragas` or `TruLens` (Faithfulness, Answer Relevance).
  - **Guardrails Engine**: Input/Output validation to prevent hallucinations and jailbreaks.

- [ ] **Module 04: Agentic — Autonomous Cognitive Architectures**
  - Fully autonomous Tool-Calling loop configuration.
  - Self-RAG paradigms (Agent evaluates if retrieved context is useful or needs re-routing).
