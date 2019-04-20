import sys
import subprocess
import json
import os
import argparse

file_name = sys.argv[1]
json_result = subprocess.check_output(['lumi', 'predict', file_name])
print("\nRSULTS WILL BE HERE ! \n")
print(json_result)
lines = json_result.splitlines()
last_line = lines[-1]
parsed_json = json.loads(last_line)

matches = 0

for match in parsed_json['objects']:
    if match['label'] == 'person':
        matches += 1
        print(match)

