"""
Collect.py
connects to arXiv, Downloads the papers for each sub-topic and saves them in one table (.CSV file)
And saved them to data/corpus.csv
"""

import arxiv
import pandas as pd

SubTopics = { 
    # Each sub topic maps to an arXiv query
    # cat = category, abs: abstract
    # We use abstract here instead of the title because it gets more results

    "object detection" : 'cat:cs.CV AND abs:"object detection"',
    "image segmentation" : 'cat:cs.CV AND abs:"image segmentation"',
    "image generation" : 'cat:cs.CV AND abs:"image generation"',
    "medical image analysis" : 'cat:cs.CV AND abs:"medical image analysis"'
}

maxPerTopic = 120 # 480 before cleaning, Should be 400+ after
client = arxiv.Client(page_size = 100, delay_seconds = 3, num_retries = 3) # Connects to arXiv and fetches results
papers = []

for subTopic, query in SubTopics.items():
    search = arxiv.Search( # Describes what to find for each sub topic
        query = query,
        max_results = maxPerTopic,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    

    for paper in client.results(search): # Gives papers one by one
        papers.append(
            {
                 "arxiv_id" : paper.entry_id,
                "title" : paper.title,
                "abstract" : paper.summary, 
                "subtopic" : subTopic,
                "pdfUrl" : paper.pdf_url,
                "primaryCategory" : paper.primary_category,
                "comment" : paper.comment
            }
        )

df = pd.DataFrame(papers)
df = df[df["primaryCategory"] == "cs.CV"] # Filtering, Keeping papers that are related to cs.CV
df = df.drop_duplicates(subset="arxiv_id") 

print(df.shape)
print(df["subtopic"].value_counts())
df.to_csv("data/corpus.csv", index = False)