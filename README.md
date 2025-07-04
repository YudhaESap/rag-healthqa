# rag-healthqa

A lightweight Retrieval-Augmented Generation (RAG) system designed to answer health-related questions using FAISS for vector search and HuggingFace Transformers for generation.

This project demonstrates how to build a simple pipeline for semantic retrieval + LLM-based answer synthesis — useful for medical knowledge bases, health tech QA, or education bots.

---

## Features

- Vector similarity search using FAISS
- Sentence embeddings with `sentence-transformers`
- LLM-based answer generation using `transformers` or OpenAI API
- Traced responses with input → context → answer flow

---

## 🧠 Stack

- Python 3.10+
- FAISS
- Sentence Transformers
- Transformers (Hugging Face)
- OpenAI (or any local LLM)
- Pandas
- Jupyter Notebook
- Streamlit (optional)

---

## Quick Start

1. Clone this repo  
   `git clone https://github.com/YudhaESap/rag-healthqa.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the notebook  
   `jupyter notebook notebook/rag_pipeline.ipynb`

---

## Sample Query

> **Prompt:** What are the symptoms of chronic kidney disease?

→ Retrieved context:
> "CKD symptoms include swelling, fatigue, and changes in urination."

→ LLM Response:
> "Common symptoms of chronic kidney disease are fatigue, swelling in legs or ankles, and frequent urination."

✅ Grounded  
✅ No hallucinations  
✅ Uses top result

---

## Project Structure

rag-healthqa/
- data/ # Sample medical articles
- src/ # Python scripts for retrieval & generation
- notebook/ # Jupyter notebook for the full pipeline
- examples/ # Prompt & answer samples
- requirements.txt
- README.md


---

##  Author

**Yudha E. Saputra**  
AI Researcher · NLP · Semantic Search · Prompt Optimization  
[LinkedIn](https://linkedin.com/in/yudhaesaputra)
