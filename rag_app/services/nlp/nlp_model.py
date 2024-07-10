from transformers import BertTokenizer, BertModel
import torch

class NLPModel:
    def __init__(self, model_name='bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        
    def encode(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).detach().numpy().flatten()
    
    @staticmethod
    def str_from_list(results):
        if len(results) > 1:
            return ", ".join(results[:-1]) + ", and " + results[-1]
        else:
            return results[0]

    def generate_response(self, results, query):

        if results:
            return f"The most similar results to '{query}' are '{self.str_from_list(results)}' respectively."
        else:
            return f"No similar results found for '{query}'."
