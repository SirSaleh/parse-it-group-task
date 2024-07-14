from fastapi import APIRouter, HTTPException

from rag_app.controllers.text_controller import TextController
from rag_app.schemas.text_schema import TextDataSchema

router = APIRouter()
controller = TextController()

@router.post("/", status_code=201)
async def add_text_data(text_data: TextDataSchema):
    """Creats a new entry for the texts
    """
    controller.add_text_data(text_data.text)
    return {"message": "Data added successfully"}

@router.get("/")
async def search_text_data(text: str, k: int = 5):
    """search for k nearest neighbors in L2 Metric
    """
    try:
        results = controller.search_text_data(text, k)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
