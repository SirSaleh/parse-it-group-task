from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from rag_app.controllers.text_controller import TextController
from rag_app.services.implementations.faiss_db import FAISSDatabase

router = APIRouter()

class TextDataSchema(BaseModel):
    text: str

class QuerySchema(BaseModel):
    query: str
    k: int

controller = TextController()

@router.post("/")
async def add_text_data(text_data: TextDataSchema):
    controller.add_text_data(text_data.text)
    return {"message": "Data added successfully"}

@router.get("/")
async def search_text_data(text: str, k: int = 5):
    try:
        results = controller.search_text_data(text, k)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
