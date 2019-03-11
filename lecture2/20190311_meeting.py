ob = "we love python "
print(type(ob))

numbers = [34, 143, 3, 53, 4]
print(type(numbers))

x = None
print(type(x))

countries = {'israel': 'jerusalem', 'italy': 'rome',
             'france': 'paris'}
print(countries)
print(type(countries))
cars = {'84-185-33': {'color': 'white', 'brand': 'honda', 'model': 'hatchback'},
        '65-767-22': {'color': 'red', 'brand': 'toyota', 'model': 'corolla'},
        '43-658-31': {'color': 'blue', 'brand': 'fiat', 'model': 'uno'}}

print(cars['84-185-33'])

# what is set ? set is a collection of UNIQUE objects

numbers = {34, 54, 6, 75, 654, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7}  # definition if a set NOT A DICT !
print(numbers, type(numbers))
print(dir(numbers))

import json

options = (dir(json))
print(type(options))

# why the fuck this works
for option in options:
    if not option.find("_"):
        options.remove(option)
    else:
        print(option)

    # print(type(option))
    #
# set and frozen set
names = {'bob', 'alice', 'sasha', 'gal', 45, 45, 34}
names.add('klaus')
print(names, "added klaus cause its mutable")
print(cars.get('84-185-33'))
print(cars.get('non-Existent-key-return-None'))
# tuple might be used for database entries in order to eliminate errors
num = 3.8
numA = int(num)
print(numA)

# non decimal numbers
octo_num = 0o14

print(type(octo_num))

hexanum = 0x14A
print(hexanum)

bina_num = 0b1001
print(bina_num)
starting_number = 14850
ob = hex(starting_number)
print(ob)
ob = bin(starting_number)
print(ob)

from decimal import Decimal

r = Decimal(0.3) + Decimal(0.12444)
print(r)
from fractions import Fraction

numX = Fraction(3, 8)  # b (3 / 8)
numY = Fraction(2, 4)  # (1 / 2)
numZ = numX + numY
print(numZ)

import sys

a = [1, 2, 34, 5, 6, ]
b = a
c = a
d = a
e = a

print(sys.getrefcount(a))  # number of instance occurrences
