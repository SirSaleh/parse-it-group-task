from rag_app.services.factories.db_factory import DatabaseFactory
from rag_app.services.nlp.nlp_model import NLPModel
from rag_app.config.settings import settings
from typing import List

class RAGController:
    def __init__(self):
        self.text_db = DatabaseFactory.create_database('faiss', 'text_data', settings.TEXT_DIMENSION)
        # self.audio_db = DatabaseFactory.create_database(settings.AUDIO_DIMENSION)
        # self.image_db = DatabaseFactory.create_database(settings.IMAGE_DIMENSION)
        self.nlp_model = NLPModel()

    def retrieve_and_generate(self, query: str, k: int):
        query_vector = self.nlp_model.encode(query)
        text_results = self.text_db.search(query_vector, k)
        # TODO: add same for audio and other datatypes in future
        response = self.nlp_model.generate_response(text_results, query)
        
        return response
