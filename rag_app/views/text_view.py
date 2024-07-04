from fastapi import APIRouter
from rag_app.controllers.text_controller import TextController
from rag_app.schemas.text_schema import TextDataSchema, QuerySchema

router = APIRouter()
controller = TextController()

@router.post("/add/")
async def add_text_data(text_data: TextDataSchema):
    controller.add_text_data(text_data.text, text_data.vector)
    return {"message": "Text data added successfully"}

@router.post("/search/")
async def search_text(query: QuerySchema):
    results = controller.search_text(query.vector, query.k)
    return {"results": results}
