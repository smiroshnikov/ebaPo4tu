import random
import json
import os
import string

FILENAME = 'E:\Development\ebaPo4tu\playground\linux_academy\cointains_test\words2'
FILENAME_W = "C://Users//Sergeim//IdeaProjects//ebaPo4tuPython//playground//linux_academy//cointains_test//words2"
data_folder = "E://Development//ebaPo4tu//playground//linux_academy//random_json//receipts//new"
data_folder_w = "C://Users//Sergeim//IdeaProjects//ebaPo4tuPython/playground//linux_academy//random_json//receipts//new"

os.environ["FILE_COUNT"] = str(5)

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip("'") for word in open(FILENAME_W).readlines()]

for id in range(count):
    amount = random.uniform(1.0, 1000.0)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount,
        'meaningless text': ''.join(random.choices(string.ascii_lowercase +
                                                   string.ascii_uppercase +
                                                   string.digits, k=random.randint(1, 5000))),
        'meaningless_ID': ''.join(random.choices(string.digits, k=random.randint(10, 15)))
    }
    with open(f"{data_folder_w}//receipt-{id}.json", 'w') as f:
        json.dump(content, f)
