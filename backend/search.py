import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("data/paper_index.faiss")
df = pd.read_csv("data/papers_meta.csv")

def search(query, k=5):
    q_embedding = model.encode([query])
    distances, indices = index.search(np.array(q_embedding), k)

    results = []
    for idx in indices[0]:
        results.append({
            "title": df.iloc[idx]["title"],
            "abstract": df.iloc[idx]["abstract"]
        })
    return results
