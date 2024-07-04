from rag_app.services.factories.db_factory import DatabaseFactory
from rag_app.config.settings import settings
from typing import List

class TextController:
    def __init__(self, db_type: str = 'faiss'):
        self.db = DatabaseFactory.create_database(db_type, 'text_data', settings.TEXT_DIMENSION)
    
    def add_text_data(self, text: str, vector: List[float]):
        self.db.add_vector(vector, text)
    
    def search_text(self, vector: List[float], k: int):
        return self.db.search(vector, k)
