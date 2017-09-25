import re
import argparse
import string


def insert_char(word, index, c):
    if index == 0:
        return(c + word)
    elif index + 1 == len(word):
        return(word + c)
    else:
        return(word[:index] + c + word[index+1:])


if __name__ == '__main__':
    # ArgumentParser
    parser = argparse.ArgumentParser(description='spell checker')
    parser.add_argument('-f',
                        type=str,
                        metavar='',
                        help='file to spell check',
                        required=True)
    args = parser.parse_args()

    with open('dictionary.txt', 'r') as f:
        dictionary = f.read().splitlines()

    # Spell checking
    mispelled = list()
    with open(args.f, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if re.findall(r"[0-9]", word):
                    continue
                word = word.lower()
                word = word.translate(str.maketrans('', '',
                                                    string.punctuation))
                if word not in dictionary:
                    mispelled.append(word)

    # Spell suggestions
    suggestions = list()
    for word in mispelled:
        for index, char in enumerate(word):
            for c in string.ascii_lowercase:
                suggestion = insert_char(word, index, c)
                if suggestion in dictionary:
                    suggestions.append(suggestion)

    print(suggestions)
