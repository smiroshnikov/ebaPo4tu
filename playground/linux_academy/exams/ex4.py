import argparse
import os
import subprocess


def get_os_type():
    if os.name == 'nt':
        return False
    else:
        return True


parser = argparse.ArgumentParser()
parser.add_argument('port_number', help='port number to kill ')

# proc = subprocess.run(["cmd", "/c", "dir"])
proc = subprocess.run(["cmd", "/c", 'netstat -a -n -o | find "5500"'])

print(proc)
