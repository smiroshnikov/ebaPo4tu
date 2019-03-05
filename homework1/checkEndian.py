import sys


def check_endian():
    return f"The system endianness is {sys.byteorder}"


print("Starting test ....\n")
print(check_endian())

print(sys.version)