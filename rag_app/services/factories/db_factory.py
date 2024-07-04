from rag_app.services.implementations.milvus_db import MilvusDatabase
from rag_app.services.implementations.faiss_db import FAISSDatabase

class DatabaseFactory:
    @staticmethod
    def create_database(db_type: str, collection_name: str, dimension: int):
        if db_type == 'milvus':
            return MilvusDatabase(collection_name, dimension)
        elif db_type == 'faiss':
            return FAISSDatabase(dimension)
        else:
            raise ValueError(f"Unknown database type: {db_type}")
