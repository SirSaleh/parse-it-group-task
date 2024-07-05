from transformers import pipeline
from rag_app.config.settings import settings

class NLPModel:
    def __init__(self):
        self.generator = pipeline("text-generation", model=settings.NLP_MODEL_PATH)

    def generate_response(self, context: str, query: str):
        prompt = f"Context: {context}\nQuery: {query}\nAnswer:"
        result = self.generator(prompt, max_length=50, num_return_sequences=1)
        return result[0]["generated_text"].split("Answer:")[1].strip()
