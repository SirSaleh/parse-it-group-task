from rag_app.services.implementations.faiss_db import FAISSDatabase
from rag_app.services.nlp.nlp_model import NLPModel

class TextController:
    def __init__(self, db: FAISSDatabase, nlp_model: NLPModel):
        self.db = db
        self.nlp_model = nlp_model

    def add_text_data(self, text: str):
        vector = self.nlp_model.encode(text)
        self.db.add_vector(vector, text)

    def search_text_data(self, query: str, k: int):
        query_vector = self.nlp_model.encode(query)
        return self.db.search(query_vector, k)
