import os
import pathlib
from textProcessor import *

filesPath = os.path.dirname(os.path.abspath(__file__))
dataPath = filesPath + "\\..\\..\\InformationRetrieval\\IR_data\\AP_DATA\\ap89_collection\\"
#dataPath = filesPath + "\\..\InformationRetrieval\IR_data\AP_DATA\ap89_collection\\"


def getStopWordsasList():
    stopWordPath = filesPath + "\\stoplist.txt"
    stopWordsDict = dict()
    stopFile = open(stopWordPath, "r")
    for stopWord in stopFile:
        stopWord = stopWord.strip()
        if len(stopWord) > 0:
            stopWordsDict[stopWord] = 1
    return stopWordsDict        

stopWordsDict = getStopWordsasList()
iterator = 0

for filename in os.listdir(dataPath):
    iterator += 1
    print("Indexing file " + filename + " with "+  str(iterator) + " ouf of " + str(len(os.listdir(dataPath))) + "\n")
    iterator += 1
    fileIterator = open(dataPath + "\\" + filename)
    started = ended = docNoRead = readText = False
    docNumber = textContents = ""
    doc_length = 0
    line = 0

    for fileLine in fileIterator:
        line += 1
        if "<DOC>" in fileLine:
            started = True
        elif "</DOC>" in fileLine:
            if started == False:
                raise Exception("Ending without start!") 
            ended = False
            started = False
            readText = False
            docNoRead = False
 #           print("DocNO: " + docNumber + " length: " + str(doc_length) +  "\n")
 #          print("Contents: " + textContents + "\n")
            docTokenizerInstance = DocumentTokenizer(docNumber)
            docTokenizerInstance.createInvertedIndex(textContents, stopWordsDict)
            docNumber = textContents = ""
            exit()
        elif started == True and ended == False  and docNoRead == False: #Read doc number first.
            fileLine = fileLine.replace('<DOCNO>', '')
            fileLine = fileLine.replace('</DOCNO>', '')
            fileLine = fileLine.strip()
            docNumber = fileLine
            docNoRead = True
        elif started == True and ended == False and docNoRead == True:   #Read doc text now.
            if '<TEXT>' in fileLine:
                readText = True
            elif readText == True:
                if '</TEXT>' in fileLine:
                    readText = False
                    continue
                textContents = textContents + fileLine
        else:
            print("Invalid characters in file " + filename + " at line " + str(line) + "\n")   
             

             