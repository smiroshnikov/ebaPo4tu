import os
from pathlib import Path

current_dir_name = os.getcwd()
print(current_dir_name)
filename = Path(
    "C:/Users/Sergeim/PycharmProjects/ebaPo4tu/playground/prep/cli_interaction/presudo_driver/nulldriver.driver")

print(filename.name)
print(filename.suffix)

try:
    with open(filename, 'r') as f:
        for line in f:
            print(line)
except Exception as e:
    print(f"Dude an error occurred {e}")

base_path = Path(__file__).parent
print(base_path)
file_path = (base_path / "../pseudo_driver/nulldriver.null").resolve()

print(file_path)
try:
    with open(filename, 'r') as f:
        for line in f:
            print(line)
except Exception as e:
    print(f"Dude an error occurred {e}")
