from dotenv import load_dotenv
load_dotenv()
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def format_prompt(query, contexts):
    return f"Context:\n{contexts}\n\nQuestion: {query}\nAnswer:"
