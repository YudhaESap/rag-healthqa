# RAG pipeline notebook
from src.retriever import SimpleRetriever
from src.generator import SimpleGenerator
from src.utils import format_prompt

retriever = SimpleRetriever()
generator = SimpleGenerator()

query = "What are the symptoms of chronic kidney disease?"
contexts = retriever.search(query, top_k=2)
context_str = " ".join(contexts)

print("Retrieved Contexts:")
print(context_str)

answer = generator.generate_answer(query, context_str)
print("\nGenerated Answer:")
print(answer)
