import os
from py.ManageFiles import readFromFile
from py.LCS import getSimilarityLCS
from py.Shingles import *
from py.Utils import *

text = readFromFile("pdf_1.txt")  # nuovo_documento.txt nuovo_doc.txt pdf_1.txt
k = 5  # per k-shingles

# LCS
if len(text) < 10000:
    print("LCS Similarity:")
    listLCS = getSimilarityLCS(text, 'dataset')
    print("Documenti più simili (LCS):", listLCS)

# FREQUENZA N-GRAMS REALE
print("Shingle Similarity:")
shingles = getShingles(text, k=k)
frequencies = getFrequencies(shingles)
shingleSimilarities = {}
for fileName in os.listdir('dataset'):
    #print(fileName + ":")
    currText = readFromFile(os.path.join('dataset', fileName))
    currShingles = getShingles(currText, k=k)
    #if fileName != "pdf_pdf.txt": print(currShingles)
    #currFrequencies = getFrequencies(currShingles)
    #if fileName != "pdf_pdf.txt": print(currFrequencies)
    similarity = getJaccardDistance(shingles, currShingles)#getJaccardDistance\(set(currFrequencies.keys()), set(frequencies.keys()))
    shingleSimilarities[fileName] = similarity

sortedShingleSimilarities = sorted(shingleSimilarities.items(), key=lambda x: x[1], reverse=True)[:10]
print(sortedShingleSimilarities)

# LSH Locality Sensitive Hashing (3 passi: shingling, min hashing, LSH)
print("Signature Similarity:")
hashedShingles = getShingles(text, k=5, hashed=True)
datasetFolder = 'dataset'
signatureSimilarities = {}

for fileName in os.listdir(datasetFolder):
    #print(fileName + ":")
    path = os.path.join(datasetFolder, fileName)
    currText = readFromFile(path)
    currHashedShingles = getShingles(currText, k=5, hashed=True)
    #if fileName != "pdf_pdf.txt": print(currHashedShingles)
    similarity = getJaccardDistance(hashedShingles, currHashedShingles)
    signatureSimilarities[fileName] = similarity

sortedSignatureSimilarities = sorted(signatureSimilarities.items(), key=lambda x: x[1], reverse=True)
print(sortedSignatureSimilarities)

# TODO: pagina 187 del PDF
