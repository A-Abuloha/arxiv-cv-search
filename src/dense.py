import pandas as pd
from sentence_transformers import SentenceTransformer as st
from sklearn.metrics.pairwise import cosine_similarity

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


def search(query):
    query_emb = model.encode([query])
    dense_scores = cosine_similarity(query_embedding, emb)[0]
    top_10 = dense_scores.argsort()[::-1][:10]

    return top_10
