import argparse

# FILENAME = 'usr/share/dict/words'
FILENAME = 'E:\Development\ebaPo4tu\playground\linux_academy\cointains_test\words2'

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial or complete string to search')

args = parser.parse_args()
snippet = args.snippet.lower().strip("'")
# had to add this on windows , go figure, dos2unix issue i guess
# TODO check this at work tomorrow
print(f"snippet is {snippet}")

with open(FILENAME) as f:
    words = f.readlines()

matches = []

for word in words:
    # print(word.lower())
    print(f"SNIPPET->>type {type(snippet)} , value {snippet}")
    print(f"WORD -->> type {type(word)} , value {word.lower()}")
    if snippet in word.lower():
        matches.append(word)

print(matches)

# one liner
# [RETURN/APPEND/RESULT  - FOR LOOP  - CONDITION]
snippet = 'serg'.strip("'")
print([word.upper() for word in words if snippet in word.lower()])

