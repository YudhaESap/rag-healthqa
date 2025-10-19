# app.py
from dotenv import load_dotenv
load_dotenv()
import argparse
from src.retriever import SimpleRetriever
from src.generator import SimpleGenerator

# Parse command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, required=True)
args = parser.parse_args()
query = args.query

# Initialize retriever and generator
retriever = SimpleRetriever()
generator = SimpleGenerator()

# Retrieve contexts
contexts = retriever.search(query, top_k=2)
print("Retrieved Contexts:\n")
print("\n---\n".join(contexts))

# Generate answer
context_str = " ".join(contexts)
answer = generator.generate_answer(query, context_str)
print("\nGenerated Answer:")
print(answer)
