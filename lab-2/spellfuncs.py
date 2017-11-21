import re
import string
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
                print(word)
                tokens.remove(word)
        return(tokens)
