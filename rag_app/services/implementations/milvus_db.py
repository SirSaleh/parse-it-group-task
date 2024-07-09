from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
from typing import List
from rag_app.services.interfaces.vector_db_interface import VectorDatabaseInterface

class MilvusDatabase(VectorDatabaseInterface):
    def __init__(self, collection_name: str, dimension: int):
        self.collection_name = collection_name
        self.dimension = dimension
        connections.connect(host="127.0.0.1", port="19530")
        
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="metadata", dtype=DataType.VARCHAR, max_length=65535),
            FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=dimension),
        ]
        schema = CollectionSchema(fields, description=f"{collection_name} collection")
        self.collection = Collection(name=collection_name, schema=schema)
        
        if not self.collection.has_index():
            self.collection.create_index(field_name="vector", index_params={"index_type": "IVF_FLAT", "metric_type": "L2", "params": {"nlist": 128}})

    def add_vector(self, vector: List[float], metadata: str):
        data = [
            [None],
            [metadata],
            [vector]
        ]
        self.collection.insert(data)
        self.collection.flush()

    def search(self, query_vector: List[float], k: int = 4):
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        result = self.collection.search([query_vector], "vector", search_params, limit=k)
        return [hit.entity.metadata for hit in result[0]]
