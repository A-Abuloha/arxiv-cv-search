

import pandas as pd

df = pd.read_csv("data/corpus.csv")

print(df.head())


# Check the number of documents and preview the first 400 characters of the first one.

documents = (
    df["title"].fillna("") + ". " + df["abstract"].fillna("")).tolist()

print("Number of documents:", len(documents))
print("\nFirst document preview:", documents[0][:400])


#We use SentenceTransformer to convert text into numerical vectors which allows us to compare the papers and the queries by the meaning

from sentence_transformers import SentenceTransformer as st

#use  the all-MiniLM-L6-v2 because it is a lightweight, fast model that converts text into  embeddings that find research papers with similar meanings

model = st("all-MiniLM-L6-v2")

# Convert each document's title and abstract into an embedding.

emb = model.encode(documents)



queries = ["Deep learning methods for real-time object detection in images",
"Using convolutional neural networks to segment objects in images",
"Detecting brain tumors in MRI scans using deep learning"]

#We have to encode the queries the same way we did with the documents to compare with the encoded documents


query_emb = model.encode(queries)

print(query_emb.shape)


# We will use cosine similarity to compare the query embeddings with the document embeddings. It gives a similarity score from -1 to 1, where a higher score
# means the document is more similar to the query. The document with the
# highest score is ranked as the most relevant result.

from sklearn.metrics.pairwise import cosine_similarity as cs

score = cs(query_emb,emb)
print(score.shape) 

#loop through all 3 queries and compare its similarity scores with the research papers and display top 10 similar papers ranked from hihgest to lowest

for i in range(len(queries)):
    query_scores = score[i]

    top_10 = query_scores.argsort()[-10:][::-1]

    print("\nQuery:", queries[i])

    for idx in top_10:
        print("Title:", df.iloc[idx]["title"])
        print("Similarity:", query_scores[idx], "\n")
   




