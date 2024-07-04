from typing import List
from rag_app.services.interfaces.vector_db_interface import VectorDatabaseInterface
import faiss
import numpy as np

class FAISSDatabase(VectorDatabaseInterface):
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add_vector(self, vector: List[float], metadata: str):
        self.index.add(np.array([vector], dtype=np.float32))
        self.metadata.append(metadata)

    def search(self, query_vector: List[float], k: int = 4):
        D, I = self.index.search(np.array([query_vector], dtype=np.float32), k)
        return [self.metadata[i] for i in I[0] if i != -1]
