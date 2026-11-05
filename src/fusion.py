import bm25
import dense
from sklearn.metrics.pairwise import cosine_similarity


def hybrid_search(query, top_k=10):
    if not query.strip():
        return []

    # Get actual BM25 results for the query.
    bm25_results = bm25.search(query)

    # Convert the query into an embedding.
    query_embedding = dense.model.encode([query])

    # Compare it with every document embedding.
    dense_scores = cosine_similarity(query_embedding, dense.emb)[0]


    # Combine both rankings using Reciprocal Rank Fusion.
    fusion_scores = {}
    k = 60

    # Add BM25 contributions.
    rank = 0

    for result in bm25_results:
        rank = rank + 1

        score = result[0]
        idx = int(result[1])

        if score > 0:
            if idx not in fusion_scores:
                fusion_scores[idx] = 0.0

            contribution = 1 / (k + rank)
            fusion_scores[idx] = fusion_scores[idx] + contribution

    # Add dense contributions.
    rank = 0

    for idx in dense_indices:
        rank = rank + 1
        idx = int(idx)

        if idx not in fusion_scores:
            fusion_scores[idx] = 0.0

        contribution = 1 / (k + rank)
        fusion_scores[idx] = fusion_scores[idx] + contribution

    # Prepare the scores for sorting.
    score_list = []

    for idx in fusion_scores:
        score = fusion_scores[idx]
        score_list.append((score, -idx))

    # Sort highest score first.
    score_list.sort(reverse=True)

    # Store results as (document position, fusion score).
    ranked_results = []

    for item in score_list:
        score = item[0]
        idx = -item[1]

        ranked_results.append((idx, score))

    return ranked_results[:top_k]


# Let the user enter a query when running this file.
if __name__ == "__main__":
    query = input("\nEnter your search: ")
    results = hybrid_search(query)

    print("\nFusion results:")

    rank = 0

    for result in results:
        rank = rank + 1

        idx = result[0]
        score = result[1]
        title = bm25.corpusDF.iloc[idx]["title"]

        print(f"\n{rank}. {title}")
        print(f"Fusion score: {score:.6f}")

    if not results:
        print("No results.")
