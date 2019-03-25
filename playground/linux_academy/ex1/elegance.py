import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file to read')
parser.add_argument('line_number', type=int, help='numerical value of line to read ')

args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number - 1]
except IndexError:
    print("Invalid line number , file has less lines! ")
except IOError as e:
    print(f"Error: {e}")
else:
    print(f"{line} ^--here is your line  ")



