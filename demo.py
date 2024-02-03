import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
parser.add_argument('-party', '-p', type=str)
args = parser.parse_args()
print(args)
