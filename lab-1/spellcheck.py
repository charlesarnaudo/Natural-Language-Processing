import argparse
import spellfuncs
import pprint

if __name__ == '__main__':
    # ArgumentParser
    parser = argparse.ArgumentParser(description='spell checker')
    parser.add_argument('-f',
                        type=str,
                        metavar='',
                        help='file to spell check',
                        required=True)
    args = parser.parse_args()

    # Create dictionary
    with open('dictionary.txt', 'r') as dictionary:
        spellfuncs = spellfuncs.SpellFuncs(dictionary)

    # Spell checking
    with open(args.f, 'r') as f:
        mispelled = spellfuncs.misspelled(f)

    suggestions = {}
    for word in mispelled:
        word_suggestions = spellfuncs.suggestions(word)
        suggestions.update({word: word_suggestions})

    pprint.pprint(suggestions)
