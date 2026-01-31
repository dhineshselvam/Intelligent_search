import json
import pandas as pd

with open("data/arxiv_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

papers = []

for paper in data:
    papers.append({
        "id": paper.get("id", ""),
        "title": paper.get("title", ""),
        "abstract": paper.get("summary", "")   # FIX HERE
    })

df = pd.DataFrame(papers)
df.to_csv("data/clean_papers.csv", index=False)

print(f"Indexed {len(df)} papers")
