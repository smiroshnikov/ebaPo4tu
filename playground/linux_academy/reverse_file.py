import argparse
import json


# build parser
# parse arguments
# read the file , reverse the content and print


parser = argparse.ArgumentParser(description="This is a reverse file reader!")  # constructing object from a class
parser.add_argument('filename', help='the file to read ')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')

parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s 1.0')  # due to this line containing an action
# it takes 'branch' in an action and if -v argument is provided will perform an action and EXIT


args = parser.parse_args()  # returns a namespace object with info pulled from flags

# print("REVERSING EVERYTHING ")
with open(args.filename) as f:
    pass
    lines = f.readlines()
    # print(lines.reverse()) # will evaluate to None
    print(type(lines))

    for ix, line in enumerate(lines):
        # I want to reverse the order of lines only not hte strings
        # print(lines[(len(lines) - ix) - 1], end="")
        print(line)

        # print(lines[len(lines) - int(lines[line])])

# Accessing index in for loop
ls = ['a', 'b', 'c']
for idx, val in enumerate(ls):
    print(idx, type(idx))
