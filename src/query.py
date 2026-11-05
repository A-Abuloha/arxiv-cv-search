from bm25 import docFreq, corpusDF
from preprocess import preProcess

def editDistance(text, text2):
    rows = len(text) + 1
    cols = len(text2) + 1
    table = []

    for row in range(rows):
        table.append([0] * cols)

    for row in range(rows):
        table[row][0] = row # Rows: 0, 1, 2, 3, ...
    for col in range(cols):
        table[0][col] = col # Cols: 0, 1, 2, 3, ...

    for i in range(1, rows):
        for j in range(1, cols):

            if text[i-1] == text2[j - 1]: cost = 0
            else: cost = 1

            delete = table[i - 1][j] + 1
            insert = table[i][j - 1] + 1
            replace = table[i - 1][j - 1] + cost

            table[i][j] = min(delete, insert, replace)

    return table[rows-1][cols-1]

def correctWord(word):
    if (word in docFreq or word.isdigit() or len(word) <= 3): return word

    bestWord = word
    bestDistance = 3 # Only words 1 or 2 edits away should count as a typo

    for term in docFreq:
        distance = editDistance(word, term)

        if (distance < bestDistance): 
            bestWord = term
            bestDistance = distance

    return bestWord

abbreviations = {
    "yolo": "you only look once",
    "rcnn": "region based convolutional neural network",
    "ssd": "single shot multibox detector",
    "fpn": "feature pyramid network",
    "rpn": "region proposal network",
    "detr": "detection transformer",
    "iou": "intersection over union",
    "nms": "non maximum suppression",
    "sam": "segment anything model",
    "fcn": "fully convolutional network",
    "dsc": "dice similarity coefficient",
    "gan": "generative adversarial network",
    "vae": "variational autoencoder",
    "ddpm": "denoising diffusion probabilistic model",
    "ldm": "latent diffusion model",
    "nerf": "neural radiance field",
    "fid": "frechet inception distance",
    "mri": "magnetic resonance imaging",
    "ct": "computed tomography",
    "pet": "positron emission tomography",
    "cxr": "chest x ray",
    "oct": "optical coherence tomography",
    "wsi": "whole slide imaging",
    "cnn": "convolutional neural network",
    "vit": "vision transformer"
}

def processQuery(query):

    words = preProcess(query)
    tokens = []

    for word in words:
        if word in abbreviations: 
            tokens.append(word)
            for abb in abbreviations[word].split():
                tokens.append(abb)
        else:
            tokens.append(correctWord(word))

    return tokens

def hasPhrase(index, phrase):
    paperTitle = corpusDF.loc[index, "title"]
    paperAbstract = corpusDF.loc[index, "abstract"]

    text = paperTitle + " " + paperAbstract

    clean = ""
    for ch in text.lower():
        if (ch.isalnum()): clean += ch
        else: clean += " "

    clean = " ".join(clean.split())

    cleanPhrase = " "
    for ch in phrase.lower():
        if (ch.isalnum()): cleanPhrase += ch
        else: cleanPhrase += " "

    cleanPhrase = " ".join(cleanPhrase.split())

    if (cleanPhrase in clean): return True
    else: return False