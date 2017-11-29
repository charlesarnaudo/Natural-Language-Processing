import random
import sys
import string
import pprint

class SpellFuncs:

    def __init__(self, file):
        self.file = file
        self.tokens = list()
        self.markov = {}

    def tokenize(self):
        tokens = list()
        for line in self.file:
            tokens += line.split()
        for i, token in enumerate(tokens):
            token = token.lower()
            token = token.translate(str.maketrans('', '', string.punctuation))
            tokens[i] = token
        self.tokens = tokens

    def generate_chain(self):
        self.markov = {i: [] for i in self.tokens}
        i = 0
        for word in self.markov:
            token_copy = self.tokens[i::3]
            for token in token_copy:
                self.markov[word].append(token)
            i += 1
    
    def print_chain(self, num_of_lines):
        for i in range(num_of_lines):
            key = random.choice(list(self.markov.keys()))
            print(key + " ".join(self.markov[key]))