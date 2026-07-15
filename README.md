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
- **LLM Engine**: Ollama (Llama 3)
- **AI Proxy Gateway**: LiteLLM
- **Vector Database**: ChromaDB
- **Embeddings**: HuggingFace (Sentence-Transformers)

---

## 🔧 Getting Started

### 1. Prerequisites
Ensure you have **Ollama** installed and running locally with the Llama3 model pull:
```bash
ollama pull llama3
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
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🧭 Roadmap
- [x] **Module 01: Beginner** - Naive RAG (Inference, Simple Chunking, Vector Storage, Retrieval)
- [ ] **Module 02: Intermediate** - Advanced Retrieval (Query Rewriting, Reranking, Hybrid Search)
- [ ] **Module 03: Advanced** - Evaluation Metrics (Ragas, TruLens) & Guardrails
- [ ] **Module 04: Agentic** - Fully Autonomous Agentic RAG using tool-calling loops
