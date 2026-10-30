"""
preprocess.py
Cleans text, splits it into words, lowercases, removes stopwords.
"""

STOPWORDS = {
    # English stopwords plus a few custom scientific stopwords for the papers.
    'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 
    'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 
    'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', 
    "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 
    'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 
    'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', 
    "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 
    'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 
    'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 
    'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 
    'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 
    'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 
    'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 
    'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 
    'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 
    'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 
    'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 
    'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 
    'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 
    'yourselves', 'paper', 'propose', 'proposed', 'method', 'approach', 'results'
}

def preProcess(text):
    text = text.lower()
    clean = ""

    for char in text: 
        if char.isalnum(): # Letter or digit -> We keep it  
            clean += char
        else: 
            clean += " "

    words = clean.split()
    tokens = []

    for word in words:
        if word not in STOPWORDS:
            tokens.append(word)

    return tokens