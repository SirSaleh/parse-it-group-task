import faiss
import numpy as np
from rag_app.services.interfaces.vector_db_interface import VectorDatabaseInterface
from typing import List

class FAISSDatabase(VectorDatabaseInterface):
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add_vector(self, vector: List[float], text: str):
        vector_np = np.array([vector], dtype=np.float32)
        self.index.add(vector_np)
        self.texts.append(text)

    def search(self, query: List[float], k: int):
        query_np = np.array([query], dtype=np.float32)
        distances, indices = self.index.search(query_np, k)
        return [self.texts[idx] for idx in indices[0]]
