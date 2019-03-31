import argparse
import sys

"""
missed points 
1. File does not exist 
2. Limit argument is invalid 
3. Make something up 
"""

parser = argparse.ArgumentParser(description="This is a reverse file reader!")
# constructing object from a class
parser.add_argument('filename', help='the file to read ')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')

parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s 1.0')

args = parser.parse_args()
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error {err}")
    sys.exit(1)  # useful for investigating later on
    # classic check when writing multi level system scripts is to check that  echo $? is Non zero
    # the number is meaningless most of the time
else:
    with open(args.filename) as f:
        # here we will try/catch/except
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]  # purity huyurity :)

        for line in lines:
            print(line.strip()[::-1])  # the backward part is here !
            print(line.strip())
# finally:
#     print("Thanks for using this utility , dont forget to donate , finally was not necessary at all in here ")
# echo $? - displays latest error status . will be changed by sys.exit
