import argparse
import sys

parser = argparse.ArgumentParser("Utility that performs a copy on the universe ")
parser.add_argument("su", help="name of the existing universe ", type=int)
parser.add_argument("du", help="name of destination universe ", type=int)

argsn = parser.parse_args()

print(argsn.su, argsn.du)
print(hex(sys.hexversion))
print(sys.version_info)

for i in range(0, 100):
    print(f"DEC : {int(i)} HEX: {hex(i)} BIN {bin(i)} OCT{oct(i)}")
