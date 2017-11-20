import argparse
import pprint
import spellfuncs

if __name__ == '__main__':
	# ArgumentParser
    parser = argparse.ArgumentParser(description='concordance')
    parser.add_argument('-f',
                        type=str,
                        metavar='',
                        help='preform concordance',
                        required=True)
    args = parser.parse_args()

    with open(args.f, 'r') as f:
        spellfuncs = spellfuncs.SpellFuncs(f)
        tokens = spellfuncs.tokenize(f)
    
    print(tokens)
