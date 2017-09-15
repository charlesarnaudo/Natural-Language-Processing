import argparse

parser = argparse.ArgumentParser(description='file to spell check')

parser.add_argument('-f',
                    nargs = 1,
                    type=str,
                    metavar='<input_file>',
                    help = 'file which containts text to tweet',
                    required = True)
