from rag_app.services.factories.db_factory import DatabaseFactory
from rag_app.services.nlp.nlp_model import NLPModel
from rag_app.utils.controller_utils import get_db_search_or_empty
from rag_app.config.settings import settings

class TextController:
    def __init__(self):
        self.db = DatabaseFactory.create_database('faiss', 'text_data', settings.TEXT_DIMENSION)
        self.nlp_model = NLPModel()

    def add_text_data(self, text: str):
        vector = self.nlp_model.encode(text)
        self.db.add_vector(vector, text)

    def search_text_data(self, query: str, k: int):
        query_vector = self.nlp_model.encode(query)
        return get_db_search_or_empty(self.db, query_vector, k)
