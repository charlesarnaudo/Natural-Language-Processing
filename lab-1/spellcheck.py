import re
import argparse
import string
import spellfuncs
import texttable as tt


def print_suggestions(mispelled, suggestions):
    """
    """
    table = tt.Texttable()
    headings = ['mispelled', 'suggestions']
    table.header(headings)

    mispelled = mispelled
    suggestions = suggestions
    for row in zip(mispelled, suggestions):
        table.add_row(row)

    print(table.draw())


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

    spellfuncs = spellfuncs.SpellFuncs(dictionary)

    # Spell checking
    mispelled = list()
    with open(args.f, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = spellfuncs.spellcheck(word)
                if word not in dictionary:
                    mispelled.append(word)


    ## Spell suggestions
    suggestions = spellfuncs.suggestions(mispelled)
    print(suggestions)

    #for word in mispelled:
    #    for index, char in enumerate(word):
    #        # Inserting chars
    #        for c in string.ascii_lowercase:
    #            suggestion = insert_char(word, index, c)
    #            if suggestion in dictionary:
    #                suggestions.append(suggestion)
    #        # Removing chars
    #        suggestion = remove_char(word, index)
    #        if suggestion in dictionary:
    #            suggestions.append(suggestion)
    #        # Switching chars
    #        switch = switch_char(word, index)
    #        print(len(word))
    #        print(str(index) + " " + word + " " + switch)

    #print_suggestions(mispelled, suggestions)
