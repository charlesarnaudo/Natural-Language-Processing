import re
import string
import pprint
from nltk.corpus import stopwords

class SpellFuncs:
   
    def __init__(self, file):
        self.file = file.read().splitlines()
        self.stops = stopwords.words('english')

    def tokenize(self):
        tokens = list()
        for line in self.file:
            tokens += line.split()
        for i, token in enumerate(tokens):
            token = token.lower()
            token = token.translate(str.maketrans('', '', string.punctuation))
            tokens[i] = token
        return(tokens)
    
    def remove_function_words(self, tokens):
        for word in tokens:
            if word in self.stops:
                tokens.remove(word)
        return(tokens)

    def concord(self):
        tokens = self.tokenize()
        words = self.remove_function_words(tokens)
        d = {}

        text = self.tokenize()
        for line in text:
            for word in words:
                if word in line:
                    if word not in d:
                        d[word] = 1
                    else:
                        d[word] += 1
        print(d)
        
