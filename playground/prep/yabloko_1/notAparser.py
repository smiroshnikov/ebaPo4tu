import argparse
import sys


def populate_list(filename, separator=","):
    list_of_lines = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                list_of_lines.append(line.replace('"', '').replace(' ', '').replace('\n', '').split(separator))
        return list_of_lines
    except FileNotFoundError as e:
        print(f"DUDE FILE IS MISSING{e} !")
        sys.exit(1)


def print_csv(fl):
    for ix, e in enumerate(fl):
        if ix == 0:
            print(f"{e} <--HEADER ")
        else:
            print(f"{e} <-line #{ix}")


def print_col(fl, col):
    print(f"will print column ->{fl[0][col]} \n"
          f"press ENTER to start")
    input()
    for l in fl:
        print(l[col])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Utility to read csv files ")
    parser.add_argument('filename', type=str, help="csv file to be parsed ")
    parser.add_argument('separator', help="separator for csv file use '|' or  ',' only")

    args = parser.parse_args()  # here an args list is created
    file_lines = populate_list(args.filename)

    print_csv(file_lines)
    print_col(file_lines, 8)
