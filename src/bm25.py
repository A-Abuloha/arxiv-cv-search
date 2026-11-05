import pandas as pd
import math
from preprocess import preProcess

corpusDF = pd.read_csv("data/corpus.csv")
docs = [] 

for i in corpusDF.index:
    title = corpusDF.loc[i, "title"]
    abstract = corpusDF.loc[i, "abstract"]

    res = title + " " + abstract

    res = preProcess(res)
    docs.append(res)

N = len(docs)
docLengths = []
for doc in docs:
    docLengths.append(len(doc))
avgDocLen = sum(docLengths) / N 

docFreq = {}
for doc in docs: 
    for term in set(doc): # unique terms only
        if term in docFreq:
            docFreq[term] += 1
        else:
            docFreq[term] = 1

def idf(term):
    df = docFreq.get(term, 0) # gets the count of the term

    #IDF formula
    score = math.log((N - df + 0.5) / (df + 0.5) + 1)

    return score

def bm25Score(queryTokens, docIndex, k1 = 1.5, b = 0.75):
    doc = docs[docIndex]
    docLen = docLengths[docIndex]
    score = 0

    for term in queryTokens:
        tf = doc.count(term)

        if tf == 0:
            continue

        denom = tf + k1 * (1 - b + b * (docLen / avgDocLen))
        termScore = idf(term) * ((tf * (k1 + 1) / denom))

        score += termScore

    return score

def search(query):
    queryToken = preProcess(query)
    result = []

    for i in range(N):
        score = bm25Score(queryToken, i)
        result.append((score, i))

    result = sorted(result, reverse = True)

    return result