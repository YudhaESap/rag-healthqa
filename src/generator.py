from dotenv import load_dotenv
load_dotenv()
from transformers import pipeline

class SimpleGenerator:
    def __init__(self, model_name='gpt2'):
        self.generator = pipeline("text-generation", model=model_name)

    def generate_answer(self, query, context):
        prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
        response = self.generator(prompt, max_length=100, do_sample=True, temperature=0.7)
        return response[0]['generated_text']
