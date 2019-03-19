import subprocess
import os
import sys

if os.name == 'nt':
    proc = subprocess.run(["cmd", "/c", "dir"])
    print(proc)
    try:
        new_proc = subprocess.run(["cmd", "/c", "apop-1"], check=True)
    # the line above adds a check for process error
    # print(new_proc)  # CalledProcessError can be caught and handled
    except subprocess.CalledProcessError as err:
        print(f"Ahtung !  {err}")
        print('Make sure that command used exists on current OS ! ')
        # sys.exit(1)

else:
    proc = subprocess.run(["ls", "-l"])

print(bytes([255, 146, 246]))  # raw byte information

# print(proc.stdout.decode(bytes([255, 146, 246])))
