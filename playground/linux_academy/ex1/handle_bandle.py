import sys


def get_user_input():
    fn = input("i need a file name ")
    ln = input("i need a line number ")


def print_by_number(fn='test_file.txt', ln=4):
    try:

        with open(fn, 'r') as f:
            lines = f.readlines()

            if len(lines) < ln or ln is 0:
                sys.exit("Impossible! Check limit ! ")

            elif ln:
                lines = lines[:ln]

        print(lines[ln-1])
        # for line in lines:
        #     print(line + "\n")
    except FileNotFoundError as e:
        sys.exit(f"FILE IS MISSING {e}")


print_by_number()
