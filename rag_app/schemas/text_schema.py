from typing import List
from pydantic import BaseModel


class TextDataSchema(BaseModel):
    text: str
