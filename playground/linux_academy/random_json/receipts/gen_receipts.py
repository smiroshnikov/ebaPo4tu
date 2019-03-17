import random
import json
import os
from pathlib import Path

FILENAME = 'E:\Development\ebaPo4tu\playground\linux_academy\cointains_test\words2'
data_folder = "E://Development//ebaPo4tu//playground//linux_academy//random_json//receipts//new"
os.environ["FILE_COUNT"] = str(10)
count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip("'") for word in open(FILENAME).readlines()]

for id in range(count):
    amount = random.uniform(1.0, 1000.0)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f"{data_folder}//receipt-{id}.json", 'w') as f:
        json.dump(content, f)
