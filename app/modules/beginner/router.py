from fastapi import APIRouter, Depends, HTTPException, status
from app.modules.beginner.schemas import IngestRequest, QueryRequest, QueryResponse
from app.modules.beginner.repository.chroma_repository import ChromaRepository
from app.modules.beginner.service.rag_service import RAGService

router = APIRouter(prefix="/beginner", tags=["Beginner RAG"])

# Dependency Injection setup providers
def get_chroma_repository() -> ChromaRepository:
    return ChromaRepository()

def get_rag_service(repo: ChromaRepository = Depends(get_chroma_repository)) -> RAGService:
    return RAGService(repository=repo)

@router.post("/ingest", status_code=status.HTTP_201_CREATED)
async def ingest_document(payload: IngestRequest, service: RAGService = Depends(get_rag_service)):
    """API endpoint capturing documents to ingest into Vector Storage."""
    try:
        total_chunks = await service.ingest_document(payload.content, payload.metadata)
        return {"status": "success", "processed_chunks": total_chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion pipeline failure: {str(e)}")

@router.post("/query", response_model=QueryResponse, status_code=status.HTTP_200_OK)
async def query_rag(payload: QueryRequest, service: RAGService = Depends(get_rag_service)):
    """API endpoint implementing vector lookup and context-grounded AI generation."""
    try:
        result = await service.execute_rag(payload.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation pipeline failure: {str(e)}")
