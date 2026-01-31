from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# FastAPI app
app = FastAPI(title="Research Paper Search")

# Allow CORS (frontend can call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend folder
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

# Redirect root "/" to frontend
@app.get("/", include_in_schema=False)
def redirect_to_frontend():
    return RedirectResponse(url="/frontend/")

# Load model, FAISS index and metadata
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("data/paper_index.faiss")
df = pd.read_csv("data/papers_meta.csv")

# Pydantic model for query
class Query(BaseModel):
    query: str
    k: int = 5

# Search endpoint
@app.post("/search")
def search_endpoint(request: Query):
    q_embedding = model.encode([request.query])
    distances, indices = index.search(np.array(q_embedding).astype("float32"), request.k)

    results = []
    for idx in indices[0]:
        results.append({
            "title": df.iloc[idx]["title"],
            "abstract": df.iloc[idx]["abstract"]
        })
    return results

# Optional: API health check
@app.get("/api")
def root_message():
    return {"message": "API is running. Use POST /search to query papers."}
