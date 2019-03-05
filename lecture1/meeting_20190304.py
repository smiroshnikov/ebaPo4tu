from lecture1.calculationBrain import megascukofunction as msc

import sys

test = 10

while test is not 0:
    print(test)
    test -= 2

test = "String"

for l in test:
    print(l)

test = {(1.1, 1.0), (1.2, 2.3), (2, 3)}

a = 3

b = int('1a', base=16)  # int is a class, Question to Haim , what really happens here
print(b)  # i have overridden int constructor's default vaue
print(b.__str__())  # equivalent of toString() in Java ?


def division(f, g):
    return f // g


print(division(4, 2))

name = "Sergey Miroshnkov"
print(f"My name is {name}")


def multiply(c, d):
    return c * d


print(multiply(5, 4))
print(msc())
print(sys.version)
# packages can allow me to create modules with existing names (aka sys )
# complete all assignments from lesson 1
# watch types and operators
