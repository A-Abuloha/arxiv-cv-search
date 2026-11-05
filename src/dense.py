import pandas as pd
from sentence_transformers import SentenceTransformer as st

# Load the papers.
df = pd.read_csv("data/corpus.csv")

# Combine each paper's title and abstract.
documents = (
    df["title"].fillna("") + ". " + df["abstract"].fillna("")
).tolist()

# Load the pretrained embedding model.
model = st("all-MiniLM-L6-v2")

# Convert the papers into embeddings.
emb = model.encode(documents)
