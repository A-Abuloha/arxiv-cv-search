# arXiv Computer vision Search Engine

A search engine for 430 computer vision papers from arxiv, Built as part of a course's main project, It supports BM25, dense retrival and fusion of both, with spelling correction, abbreviations expansion, case-insensitive search and phrase matching.

## Team 5

## Corpus
- Category: cs.CV (Computer Vision)
- 430 papers across 4 sup-topics: object detection, image segementation, image generation, medical image analysis
- Length tier: short (<= 6), medium (7-9), long (>= 10)
- Collection details: 'data/collection_log.md'
- statistics report: 'reports/corpus_statistics.pdf'

## Setup
```
pip install -r requirements.txt
```

## Run
```
streamlit run app.py
```

## File Structure:<br><br>

### README.md
 --> Explains what it is, who made it, how to install it and how to run it. <br>

### requirements.txt
--> The list of pyhton libraries the project needs so anyone can install them all in one go.<br>

### app.py
--> The website the user sees, it has a search box, chooses between BM25, dense or fusion.

### src/collect.py
--> connects to arXiv, Downloads the papers for each sub-topic and saves them in one table (.CSV file)

### src/preprocess.py
--> Cleans text, splits it into words, lowercases, removes stopwords and stems.

### src/bm25.py
--> Scores papers by how well their words match the query.

### src/dense.py
--> Turns papers into vectors and finds the closest one.

### src/fusion.py
--> Merges the two ranked lists dense & BM25 into one ranking.

### src/query.py
--> Fixes the query before searching: corrects spelling, expands abbrevations 

### src/stats.py
--> Calculates numbers about the corpus for the report.

### src/add_pages.py
-->  Downloads papers, Counts pages, adds two columns "page_count" and "length_tier"

### data/corpus.csv
--> The collection of papers, one row per paper.

### data/collection_log.md
--> Queries and date range, so anyone can rebuild it. 

### ai-logs/phase1/index.md
--> Ai chats, Which tool and what it helped with.

