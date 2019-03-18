import json
import os
import re
import sys
import glob
import shutil

CURRENT_PATH = (os.path.dirname(os.path.abspath('process_receipts.py')))
ADSKIYSUKAYOBANIYPIZDETZ = 'dir new /b | findstr /i "receipt-[1-3]*.json"'
NORM_COMMAND = 'ls new/receipt-[1-3]*.json'

try:
    os.mkdir(CURRENT_PATH + "//processed")
except OSError as e:
    print(f"Folder already exists!\n{str(e).upper()}")
    # sys.exit("UNDERSTAND WHAT YOU ARE DOING ! ")

print(glob.glob('./*.*'))  # perfectly working on the fucking windows.
print(glob.glob('**/*.json', recursive=True))

receipts = glob.glob('./new/receipt-[0-9]*.json')
# print(re.sub("\D", "", receipts[0]))

subtotal = 0.0

for path in receipts:
    file_number = (int(re.sub('\D', '', path)) + 1)
    with open(path, 'r') as f:
        content = json.load(f)
        subtotal += float(content['value'])
        print(f"current subtotal is ->{subtotal}")
        print(f"Total files processed... {file_number}")

    name = path.split("/")[-1]

    destination = f".\\processed\\{name}"
    shutil.move(path, destination)

print(f"Total value in receipts counted so far is : {subtotal}")
