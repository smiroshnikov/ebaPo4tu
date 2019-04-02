temp = -2


def something():
    global temp
    temp = 12


something()
print(int(0b001))
value = 0b0001
value = hex(int(value))
n = 10


def doA():
    n = 12


def doB():
    global n
    n = 14


doA()
print(f"A : {n}")
doB()
print(f"B: {n}")



def abc():
    temp = 2

    def b():
        nonlocal temp
        temp = 4
        print(f"temp inside b {temp}")

    b()
    print(f"temp inside a {temp}")


abc()

ob = {'x': "a",
      'y': "b"}


def f(x, y):
    print(x)
    print(y)


f(**ob)  # unpacking with ** will always expect strings


def sum(*tpl):  # this is packing
    sum = 0
    for n in tpl:
        sum = sum + n
    return sum


print(sum(1, 2, 1, 1, 1, 1, 1, 9, 9, 9, 10))


def pack_to_dict(**args):
    print(args)


f1 = pack_to_dict  # expression that its value is reference to pack_to_dict object
pack_to_dict(a=2, b=3, c=5)

print(pack_to_dict.__annotations__)


def f3(country: str, food: str, str='eggs') -> int:
    print("stuff")


print(f3.__annotations__)

# called anonymous function
ob = lambda a, b, c: a + b + c  # exactly as function just without a name
print(ob)

# pros of using lambda is getting variable right away
