"""
add_pages.py
Downloads papers, counts pages, adds page_count and length_tier columns to data/corpus.csv
"""

import pandas as pd
import requests
import pymupdf
import time

df = pd.read_csv("data/corpus.csv")

# short (<= 6 pages), medium (7-9 pages), and long (>9 pages).
def get_tier(page):
    if pd.isna(page):
        return None
    
    if page <= 6:
        return "short"
    
    elif 7 <= page <= 9:
        return "medium"
    
    else:
        return "long"

def count_pages(url):
    headers = {"User-Agent" : "arxiv-cv-search student project"}
    pdf = requests.get(url, headers=headers, timeout=30).content
    doc = pymupdf.open(stream=pdf, filetype="pdf")
    return doc.page_count

if "page_count" not in df.columns:
    df["page_count"] = None

for i in df.index:
    if not pd.isna(df.loc[i, "page_count"]):
        continue

    try:
        pages = count_pages(df.loc[i, "pdfUrl"])
    except Exception as e:
        print("Error:", e)
        pages = None

    df.loc[i, "page_count"] = pages
    print(i, pages)

    df.to_csv("data/corpus.csv", index = False)

    time.sleep(3)

df["length_tier"] = df["page_count"].apply(get_tier)
print(df["length_tier"].value_counts())
df.to_csv("data/corpus.csv", index = False)