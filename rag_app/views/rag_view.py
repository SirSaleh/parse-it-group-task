from fastapi import APIRouter
from rag_app.controllers.rag_controller import RAGController
from rag_app.schemas.rag_schema import ResponseSchema

router = APIRouter()
controller = RAGController()

@router.get("/query/", response_model=ResponseSchema)
async def query_rag_system(query: str, k: int= 1):
    """generates response for RAG system
    """
    response = controller.retrieve_and_generate(query, k)
    return {"response": response}
