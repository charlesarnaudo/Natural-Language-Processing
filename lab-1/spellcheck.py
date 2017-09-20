import argparse, nltk, string

parser = argparse.ArgumentParser(description='spell checker')

parser.add_argument('-f',
                    type=str,
                    metavar='',
                    help = 'file to spell check',
                    required = True)
args = parser.parse_args()

with open('dictionary.txt', 'r') as f:
    dictionary = f.read().splitlines()

with open(args.f, 'r') as f:
    text = f.read().splitlines()
    for line in text:
        line = line.lower()
        #line = line.translate(str.maketrans(string.punctuation))
        #line = line.translate(str.maketrans('0123456789'))
        line = line.split(" ")
        for word in line:
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.translate(str.maketrans('','', '0123456789’‘“”'))
            if word not in dictionary:
                print(word)
