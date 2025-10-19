from dotenv import load_dotenv
load_dotenv()
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd

class SimpleRetriever:
    def __init__(self, csv_path='data/health_articles.csv'):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.data = pd.read_csv(csv_path)
        self.texts = self.data['text'].tolist()
        self.embeddings = self.model.encode(self.texts, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(self.embeddings)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.texts[i] for i in indices[0]]
