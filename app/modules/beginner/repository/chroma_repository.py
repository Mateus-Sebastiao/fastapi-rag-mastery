import chromadb
from chromadb.utils import embedding_functions
from app.core.config import settings

class ChromaRepository:
    """
    Repository abstraction layer responsible for direct vector database 
    communications with ChromaDB using HuggingFace local embedding models.
    """
    def __init__(self):
        # Client instantiation with persistence capability
        self.client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIR)
        
        self.embedding_fn = embedding_functions.OllamaEmbeddingFunction(
            url="http://localhost:11434",
            model_name="nomic-embed-text:v1.5"
        )
        
        # Get or create target collection instance
        self.collection = self.client.get_or_create_collection(
            name="beginner_rag_collection",
            embedding_function=self.embedding_fn
        )

    def save_chunk(self, doc_id: str, chunk: str, metadata: dict) -> None:
        """Persists a text chunk vector inside ChromaDB collection."""
        # Força um dicionário válido para evitar falhas de metadados vazios no Chroma
        meta_payload = metadata if metadata else {"source": "api_ingest"}
        
        self.collection.add(
            documents=[chunk],
            metadatas=[meta_payload],
            ids=[doc_id]
        )

    def query_similarity(self, query_text: str, n_results: int = 3) -> list[str]:
        """Queries database collection using vector similarity search."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results.get("documents", [[]])[0] if results.get("documents") else []
