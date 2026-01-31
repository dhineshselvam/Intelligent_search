import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Load cleaned data
df = pd.read_csv("data/clean_papers.csv")

# Use small & fast model (perfect for 41K papers)
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = df["abstract"].fillna("").tolist()

print("Creating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    batch_size=64
)

# Convert to numpy
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, "data/paper_index.faiss")
df.to_csv("data/papers_meta.csv", index=False)

print(f"Embeddings created for {len(df)} papers")
