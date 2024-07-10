from pydantic import BaseModel

class QuerySchema(BaseModel):
    query: str
    k: int = 4

class ResponseSchema(BaseModel):
    response: str
