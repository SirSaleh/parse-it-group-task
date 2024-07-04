from abc import ABC, abstractmethod
from typing import List

class VectorDatabaseInterface(ABC):
    @abstractmethod
    def add_vector(self, vector: List[float], metadata: str):
        raise NotImplementedError("Subclasses should implement add_vector method")

    @abstractmethod
    def search(self, query_vector: List[float], k: int):
        raise NotImplementedError("Subclasses should implement search method")
