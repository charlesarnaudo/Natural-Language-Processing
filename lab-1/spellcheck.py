import argparse
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
    with open(args.f, 'r') as f:
        mispelled = spellfuncs.misspelled(f)

    suggestions = {}
    for word in mispelled:
        word_suggestions = spellfuncs.suggestions(word)
        suggestions.update({word: word_suggestions})

    print(suggestions)
