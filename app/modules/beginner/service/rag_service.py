import uuid
from litellm import acompletion
from app.modules.beginner.repository.chroma_repository import ChromaRepository

class RAGService:
    """
    Core Domain Service orchestrating RAG pipelines for the Beginner Module.
    Bridges Data Storage Layer and AI Inference Layer.
    """
    def __init__(self, repository: ChromaRepository):
        self.repository = repository

    async def ingest_document(self, content: str, metadata: dict) -> int:
        """
        Executes basic fixed-size naive chunking strategy 
        and sends payloads to storage layer.
        """
        # Naive chunking strategy: simple slice by words length limit
        words = content.split()
        chunk_size = 100
        chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
        
        for chunk in chunks:
            doc_id = str(uuid.uuid4())
            self.repository.save_chunk(doc_id=doc_id, chunk=chunk, metadata=metadata)
            
        return len(chunks)

    async def execute_rag(self, question: str) -> dict:
        """
        Executes Naive RAG flow: Retrieval -> Augmentation -> Generation.
        Leverages LiteLLM router proxy interface mapping local Ollama engine.
        """
        # 1. Retrieval Layer
        contexts = self.repository.query_similarity(query_text=question, n_results=3)
        joined_context = "\n\n".join(contexts) if contexts else "No relevant context found."

        # 2. Augmentation Layer (System Prompt Engineering)
        system_prompt = (
            "You are a helpful senior AI Assistant. Answer the user question based strictly "
            f"on the provided Context below. If unsure, state that you do not know.\n\nContext:\n{joined_context}"
        )

        # 3. Generation Layer via LiteLLM API Gateway Proxy (Ollama/Llama3 mapping)
        response = await acompletion(
            model="ollama/llama3.2:3b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            api_base="http://localhost:11434" # Directly to local Ollama engine pipeline bypass
        )

        generated_answer = response.choices[0].message.content
        return {
            "answer": generated_answer,
            "source_documents": contexts
        }
