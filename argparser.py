import argparse

parser.argparse.ArgumentParser(
    prog = 'top',
    description = 'show top line from each line')

parser.add_argument('filename', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)