from typing import List
from pydantic import BaseModel

class TextData(BaseModel):
    id: int
    text: str
    vector: List[float]
