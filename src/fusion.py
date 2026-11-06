import bm25
import dense
from sklearn.metrics.pairwise import cosine_similarity


def hybrid_search(query, top_k=10):
    if not query.strip():
        return []

    bm25_results = bm25.search(query)
    dense_results = dense.search(query)

    fusion_scores = {}
    rank = 0

    for result in bm25_results:
        rank = rank + 1

        score = result[0]
        idx = int(result[1])

        if score > 0:
            if idx not in fusion_scores:
                fusion_scores[idx] = 0.0

            contribution = 1 / (60 + rank)    # RRF formula is used to calculate the contribution based on the paper's rank in the search results.
            fusion_scores[idx] = fusion_scores[idx] + contribution

    rank = 0

    for index in dense_results:
        rank = rank + 1
        idx = int(index)

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



