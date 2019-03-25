with open('my_file.txt', 'w') as f:
    for _ in range(1, 100):
        print(f"{_}", file=f)
a, b, *c = 1, 2, (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(type(c))  # why this is list and not tuple


# using dict as switch
def x_func():
    return 'called x'


def y_func():
    return 'called y'


def z_func():
    return 'called z'


phone_code = {
    1: x_func(),
    2: y_func(),
    3: z_func()
}
# how do i execute code from each function ?
print(phone_code[2])

s = 0
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0]:
    s = s + n
    print(f"{s}")

points = [(1, 1), (2, 2), (1, 2), (3, 0)]
for (x, y) in points:
    print(x, y)

l = [(1, 2, 3, 4, 5, 6, 7, 8), (44, 5, 3, 2, 12, 354, 23), (3, 4, 5, 6, 7445, 34, 456, 455, 223, 11)]
for (a, *b, c) in l:
    print(f"a is {a} getting FIRST ")
    print(f"b is {b} b receives values AFTER <a> and <b>")
    print(f"c is {c} getting LAST")

for (*a, b, c) in l:
    print(f"a is {a} getting ALL BESIDES 2 last  ")
    print(f"b is {b} b receives one BEFORE LAST ")
    print(f"c is {c} getting LAST")
