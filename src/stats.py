from bm25 import corpusDF, docLengths, avgDocLen, docFreq


# Domain & Retrieval Parameters, From collection_Log 

# Total Corpus Volume
totalPapers = len(corpusDF)

# Sub-Topic Distribution
papersPerSubTopic = corpusDF["subtopic"].value_counts()
subTopicPercent = round(papersPerSubTopic / totalPapers * 100, 1)

# Length Tier Breakdown
papersPerTier = corpusDF["length_tier"].value_counts()
tierPercent = round(papersPerTier / totalPapers * 100, 1)

averagePages = round(corpusDF["page_count"].mean(), 1)
minPages = corpusDF["page_count"].min()
maxPages = corpusDF["page_count"].max()

# Field Completeness
missingFields = corpusDF[["title", "abstract", "arxiv_id", "subtopic"]].isna().sum()

# Text Metrics
averageDocLength = round(avgDocLen, 1)
shortestDoc = min(docLengths)
longestDoc = max(docLengths)
vocabSize = len(docFreq)
totalWords = sum(docLengths)

print(f"Total Papers: {totalPapers}")
print("--------------------------------")
print(f"Papers Per Subtopic:\n {papersPerSubTopic}")
print(f"Sub Topic Percent :\n {subTopicPercent}")
print("--------------------------------")
print(f"Papers Per Tier:\n {papersPerTier}")
print(f"Tier Percent:\n {tierPercent}")
print(f"Average Pages: {averagePages}")
print(f"Min Pages: {minPages}")
print(f"Max Pages: {maxPages}")
print("--------------------------------")
print(f"Missing Fields:\n {missingFields}")
print("--------------------------------")
print(f"Average Doc Length: {averageDocLength}")
print(f"Shortest Doc: {shortestDoc}")
print(f"Longest Doc: {longestDoc}")
print(f"Vocab Size: {vocabSize}")
print(f"Total Words: {totalWords}")
