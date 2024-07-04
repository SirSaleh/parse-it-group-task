from typing import List
from pydantic import BaseModel

class TextDataSchema(BaseModel):
    text: str
    vector: List[float]

class QuerySchema(BaseModel):
    vector: List[float]
    k: int = 4
