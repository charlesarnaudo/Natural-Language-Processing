import argparse
import pprint
import spellfuncs

if __name__ == '__main__':
	# ArgumentParser
    parser = argparse.ArgumentParser(description='markov generate')
    parser.add_argument('-f',
                        type=str,
                        metavar='',
                        help='generate text',
                        required=True)
    args = parser.parse_args()

    with open(args.f, 'r') as f:
        spellfuncs = spellfuncs.SpellFuncs(f)
        tokens = spellfuncs.tokenize()
        tokens = spellfuncs.generate_chain()
        spellfuncs.print_chain(1)