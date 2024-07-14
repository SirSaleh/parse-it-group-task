from fastapi import APIRouter
from rag_app.controllers.rag_controller import RAGController
from rag_app.schemas.rag_schema import QuerySchema, ResponseSchema
from rag_app.services.implementations.faiss_db import FAISSDatabase

router = APIRouter()
controller = RAGController()

@router.get("/query/", response_model=ResponseSchema)
async def query_rag_system(query: str, k: int= 1):
    response = controller.retrieve_and_generate(query, k)
    return {"response": response}
