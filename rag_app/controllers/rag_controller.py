from rag_app.services.factories.db_factory import DatabaseFactory
from rag_app.services.nlp.nlp_model import NLPModel
from rag_app.config.settings import settings
from rag_app.utils.controller_utils import get_db_search_or_empty
from typing import List

class RAGController:
    def __init__(self):
        self.text_db = DatabaseFactory.create_database('faiss', 'text_data', settings.TEXT_DIMENSION)
        self.nlp_model = NLPModel()

    def retrieve_and_generate(self, query: str, k: int):
        query_vector = self.nlp_model.encode(query)
        text_results = get_db_search_or_empty(self.text_db, query_vector, k)
        response = self.nlp_model.generate_response(text_results, query)
        return response
