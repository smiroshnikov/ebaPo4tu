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
    os.mkdir(CURRENT_PATH + "\\processed")
except OSError as e:
    print(f"Folder already exists!\n{str(e).upper()}")
    # sys.exit("UNDERSTAND WHAT YOU ARE DOING ! ")

# print(glob.glob('./*.*'))  # perfectly working on the fucking windows.
# print(glob.glob('**/*.json', recursive=True))

receipts = glob.glob('./new/receipt-[0-9]*.json')
# for i in receipts:
#     folder, filename = os.path.split(i)
#     print(filename)


subtotal = 0.0

for path in receipts:
    folder, filename = os.path.split(path)
    # why full glob path is needed here ?
    with open(path, 'r') as f:
        content = json.load(f)
        subtotal += float(content['value'])
        print(f"current subtotal is ->{subtotal}")

        # TODO I want to index files , just because
        # print(f"Total files processed... {file_number}")

    destination_PATH = (os.path.dirname(os.path.abspath('process_receipts.py')) + "\\processed")
    source_PATH = (os.path.dirname(os.path.abspath('process_receipts.py')) + "\\new")
    shutil.move(source_PATH+"\\"+filename, destination_PATH+"\\"+filename)

print(f"Total value in receipts counted so far is : {subtotal}")
