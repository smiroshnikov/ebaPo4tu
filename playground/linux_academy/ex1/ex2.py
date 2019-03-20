# THIS SOLUTION IS CRAP

# file_name = input("Please provide a file name :")
#
# with open(file_name,'x') as f:
#
#     while True:
#         data = input("Please enter data : ")
#         f.write(data+"\n")
#         if data is '':
#             break
#
# A BETTER SOLUTION
import sys


def get_file_name(repromt=False):
    if repromt:
        print("Please enter a file name. ")
    # strip is just in case to remove trailing f/b
    file_name = input("Destination file name ").strip()

    return file_name or get_file_name(True)


try:

    with open(get_file_name(), 'x') as f:
        eof = False
        content = []

        while not eof:
            line = input("enter data:\n")
            if line.strip():
                content.append(f"{line}\n")
            else:
                eof = True
        f.writelines(content)
        print("content was written successfully !  ")
except FileExistsError as e:
    sys.exit(f"Great keep trying to overwrite existing file . use 'w' flag if you need {e}")
