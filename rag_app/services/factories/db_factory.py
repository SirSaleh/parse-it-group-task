# rag_app/services/factories/db_factory.py
from rag_app.services.implementations.milvus_db import MilvusDatabase
from rag_app.services.implementations.faiss_db import FAISSDatabase

class DatabaseFactory:
    _instances = {}

    @staticmethod
    def create_database(db_type: str, collection_name: str, dimension: int):
        if db_type not in DatabaseFactory._instances:
            if db_type == 'milvus':
                DatabaseFactory._instances[db_type] = MilvusDatabase(collection_name, dimension)
            elif db_type == 'faiss':
                DatabaseFactory._instances[db_type] = FAISSDatabase(dimension)
            else:
                raise ValueError(f"Unknown database type: {db_type}")
        return DatabaseFactory._instances[db_type]
