import os
from math import pi


def get_user_message():
    return input("Give me a message plz:")


def message_repeater():
    ui = input("How many time to repeat ?")
    return 1 if not ui else int(ui)


def print_da_message(message, count):
    while count != 0:
        print(message)
        count -= 1


# def pi_digits(digits=10):
def pi_digits():
    # os.environ['DIGITS'] = str(digits)
    digits = int(os.getenv("DIGITS") or 10)
    print(f"the number is {round(pi, int(digits))}")


def main():
    # message = get_user_message()
    # print_da_message(message, message_repeater())
    pi_digits()


if __name__ == "__main__":
    os.environ['DIGITS'] = str(2)
    main()
