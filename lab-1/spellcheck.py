import argparse, nltk, string

with open('dictionary.txt') as f:
    dict = f.read().splitlines()

#for word in dict:
#    print(word)

parser = argparse.ArgumentParser(description='spell checker')

parser.add_argument('-f',
                    type=str,
                    metavar='',
                    help = 'file to spell check',
                    required = True)
args = parser.parse_args()

print("Please wait...")
with open(args.f) as f:
    text = f.read().splitlines()

tokens = []

for line in text:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','','0123456789'))
    line = nltk.word_tokenize(str(line))
    for word in line:
        tokens.append(str(word).lower())

for token in tokens:
    if token not in dict:
        print(token)
