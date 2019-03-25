long_element_list = [12.5, "abc",
                     [4, 2, 53, "abnc"], {'one': 'The One', 'two': 'Two Files'},
                     (1, 'abc', 23, "A"), {'a', 'b', 'c'}, True]

for e in long_element_list:
    print(type(e))

str = "hello"
for ix, letter in enumerate(str):
    print(str[ix])

for l in str:
    print(l)

list = [12, 43, 64, 9]
sum = list[0] + list[1] + list[2] + list[3]
print(sum)

cars = {5324334, "mazda 6", "2014", "2000",
        2434343, "mazda 3", "2013", "1600",
        5234343, "ford kuga", "2014", "1500"}
print(cars)

total = 0
account = {
    5324334: (5324334, 10000, 0.02),
    2434343: (2434343, 80000, 0.01),
    5234343: (5234343, 30000, 0.02)
}

total += account.get(5324334)[1]
total += account.get(2434343)[1]
total += account.get(5234343)[1]
print(total)

numner = 1232
print(f"{bin(numner)} binary \n")
print(f"{hex(numner)} hexadecimal \n")
print(f"{oct(numner)} octal \n")

from math import fsum


def gimmeFsum(l):
    return fsum(l)


print(gimmeFsum([32, 345, 342, 4, 234]))

from fractions import Fraction


def gimmeTotalFraction(list):
    t = 0
    for e in list:
        t += Fraction(*e)
        # The * operator simply unpacks the tuple and passes them as the positional arguments to the function.
    return t


print(gimmeTotalFraction([(3, 4), (1, 7), (3, 8), (5, 9), (7, 8), (13, 17)]))


def convert_user_to_binary():
    return bin(int(input("please enter a number ")))


print(convert_user_to_binary())


def create_love_file(filename):
    f = open(filename, 'w')
    f.write("we love python!")
    f.close()


create_love_file('new_text.txt')


def read_file(filename):
    f = open(filename, 'r')
    print(f.readlines())


read_file('new_text.txt')

list = [Fraction(1, 2), Fraction(3, 4), Fraction(5, 8), Fraction(7, 8)]

copied_list = list.copy()
copied_list[0] = Fraction(897, 15644)
print(f"{list} original list")
print(f"{copied_list} copied list")


def calculate_sum(l):
    r = 0
    for n in l:
        r += n
    return r / len(l)


print(calculate_sum([1, 2, 3]))

from decimal import Decimal
from decimal import getcontext

getcontext().prec=10 # total number of digits
print(f"{Decimal(12002).sqrt()} here it is ")


