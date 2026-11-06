import bm25
import dense
from sklearn.metrics.pairwise import cosine_similarity


def hybrid_search(query, top_k=10):
    if not query.strip():
        return []

    bm25_results = bm25.search(query)
    dense_results = dense.search(query)

    print("\nBM25 rankings:")
    for rank, result in enumerate(bm25_results, start=1):
        idx = int(result[1])
        print(rank, bm25.corpusDF.iloc[idx]["title"])

    # Print Dense rankings
    print("\nDense rankings:")
    for rank, idx in enumerate(dense_results, start=1):
        idx = int(idx)
        print(rank, bm25.corpusDF.iloc[idx]["title"])


  
    fusion_scores = {}
    rank = 0

    for result in bm25_results:
        rank = rank + 1

        score = result[0]
        idx = int(result[1])

        if score > 0:
            if idx not in fusion_scores:
                fusion_scores[idx] = 0.0

            contribution = 1 / (60 + rank)
            fusion_scores[idx] = fusion_scores[idx] + contribution

    rank = 0

    for idx in dense_results:
        rank = rank + 1
        idx = int(idx)

        if idx not in fusion_scores:
            fusion_scores[idx] = 0.0

        contribution = 1 / (60 + rank)
        fusion_scores[idx] = fusion_scores[idx] + contribution


    score_list = []

    for idx in fusion_scores:
        score = fusion_scores[idx]
        score_list.append((score, idx))

    score_list.sort(reverse=True)

    ranked_results = []

    for item in score_list:
        score = item[0]
        idx = item[1]

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
