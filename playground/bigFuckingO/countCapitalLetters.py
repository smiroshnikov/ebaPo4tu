import random
import string
import sys

data_folder = "E://Development//ebaPo4tu//playground//bigFuckingO"

meaningless_text = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits,
                                          k=random.randint(4000, 240000)))


def create_letter_file():
    try:  # useless , 'x' flag creates a new one
        with open('lettersFile.txt', 'x') as f:
            f.write(meaningless_text)
    except FileExistsError as e:
        print(f'{e} + idiot! ')
        sys.exit("file exists , aborting")


def one_liner_count_capital(list):
    # works as well
    return len([letter for letter in list if letter in string.ascii_uppercase])


def count_capital_letters_in_file(filename):
    cap_letter_list = []
    try:
        with open(filename) as f:
            megastring = f.readline()

            x = one_liner_count_capital(megastring)
            # for letter in megastring:
            #     if letter in string.ascii_uppercase:
            #         cap_letter_list.append(letter)
            # return len(cap_letter_list)
            return x

    except FileNotFoundError as e:
        sys.exit(f"File is missing {str(e).upper()}")


print(count_capital_letters_in_file("lettersFile.txt"))
print(count_capital_letters_in_file("testLetterFile.txt"))
