import sys
sys.path.append("src")
import bm25, query
import streamlit as st

st.title("arXiv Computer Vision Search")
userQuery = st.text_input("Search")
model = st.selectbox("Model", ["BM25", "Dense", "Fusion"])
phraseOnly = st.checkbox("Match exact phrase")

if userQuery:
    tokens = query.processQuery(userQuery)
    fixedQuery = " ".join(tokens)
    results = bm25.search(fixedQuery)

    resultList = []
    for score, i in results:
        if (score > 0): resultList.append((score, i))

    if phraseOnly:
        phraseList = []
        for score, i in resultList:
            if query.hasPhrase(i, userQuery): phraseList.append((score, i))
        resultList = phraseList

    resultList = resultList[:10]

    for score, i in resultList:
        title = bm25.corpusDF.loc[i, "title"]
        link = bm25.corpusDF.loc[i, "arxiv_id"]
        snippet = bm25.corpusDF.loc[i, "abstract"][:200]

        st.markdown(f"### [{title}]({link})")
        st.write(f"Score: {round(score, 2)}")
        st.write(snippet + "...")
        st.divider()
        
