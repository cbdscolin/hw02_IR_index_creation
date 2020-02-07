import string

class DocumentTokenizer:
    def __init__(self, docId):
        self.docId = docId
        self.tokenData = dict()
    
    def createInvertedIndex(self, textContents, stopWordsDict):
        tokenArray = textContents.split()
        tokenPosition = 0
        for textToken in tokenArray:
            textToken = textToken.translate(str.maketrans('', '', string.punctuation))
#            if tokenPosition >= 409:
#                print("abc")
            textToken = textToken.lower()
            textToken = textToken.strip()
            if len(textToken) <= 0 or textToken in stopWordsDict:
                continue
            tokenPosition += 1
            print(textToken)

            
