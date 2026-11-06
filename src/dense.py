import pandas as pd
from sentence_transformers import SentenceTransformer as st
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("data/corpus.csv")

# Combine each paper's title and abstract.
documents = (
    df["title"].fillna("") + ". " + df["abstract"].fillna("")
).tolist()


model = st("all-MiniLM-L6-v2")

# Convert the papers into embeddings.
emb = model.encode(documents)



# False returns only paper indices for Fusion ,RRF uses ranks, not cosine similarity scores
# True returns paper indices and cosine similarity scores for the GUI.
def search(query, return_scores=False):     
    query_emb = model.encode([query])
    dense_scores = cosine_similarity(query_emb, emb)[0]
    top_10 = dense_scores.argsort()[::-1][:10]

    if return_scores:
        results = []

        for i in top_10:
            score = float(dense_scores[i])
            idx = int(i)

            results.append((score, idx))

        return results

    return top_10

 
