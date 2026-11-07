import sys
sys.path.append("src")
import bm25, dense, fusion, query
import streamlit as st

st.title("arXiv Computer Vision Search")
userQuery = st.text_input("Search")
model = st.selectbox("Model", ["BM25", "Dense", "Fusion"])
phraseOnly = st.checkbox("Match exact phrase")

if userQuery:
    tokens = query.processQuery(userQuery)
    fixedQuery = " ".join(tokens)
    resultList = []

    if model == "BM25":
        results = bm25.search(fixedQuery)

        for score, i in results:
            if score > 0:
                resultList.append((score, i))

    elif model == "Dense":
        results = dense.search(fixedQuery, return_scores=True)

        for score, i in results:
            resultList.append((score, i))

    elif model == "Fusion":
        results = fusion.hybrid_search(fixedQuery, top_k=len(bm25.corpusDF))

        for i, score in results:
            resultList.append((score, i))

    if phraseOnly:
        phraseList = []
        for score, i in resultList:
            if query.hasPhrase(i, userQuery): phraseList.append((score, i))
        resultList = phraseList

    resultList = resultList[:10]
    if not resultList:
        st.write("No results found.")


    for score, i in resultList:
        title = bm25.corpusDF.loc[i, "title"]
        link = bm25.corpusDF.loc[i, "arxiv_id"]
        snippet = bm25.corpusDF.loc[i, "abstract"][:200]

        st.markdown(f"### [{title}]({link})")
        st.write(f"Score: {score:.6f}")

        words = snippet.split()
        highlighted = []
        for word in words: 
            clean = word.lower().strip(".,;:()")
            if clean in tokens: 
                highlighted.append("**" + word + "**")
            else:
                highlighted.append(word)
        st.markdown(" ".join(highlighted) + "...")

        st.divider()

