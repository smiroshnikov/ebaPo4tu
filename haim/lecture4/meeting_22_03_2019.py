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


def multiplication_table(limit=10):
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            print(f"{x}*{y}="
                  f"{x * y}", end='\t')
        print("\n")


multiplication_table(20)
# cool
with open('meeting_22_03_2019.py', 'r') as f:
    for line in f:
        print(line.strip(), end="")

print(end="\n")
print([n * n for n in [1, 2, 3, 4, 5, 5] if n % 2 == 0])

vec_a = [1, 2, 3, 4, 5]
vec_b = [5, 4, 3, 2, 1]
vec_c = [11, 12, 13, 14, 15]

print([x * y * z for x in vec_a for y in vec_b for z in vec_c])


# map function

def f(n):
    return n * 7


nl = map(f, [1, 2, 3, 4, 5, 6, 7])
print([v for v in nl])

names = {'dave', 'bob', 'muki', 'kuki', 'xiiii'}


def get_len(name):
    return len(name)


nll = map(get_len, names)  # PAY ATTENTION name only without ()
print([n for n in nll])

# zip function combines stuff
countries = ['il', 'sw', 'ita', 'cad']
capitals = ['jer', 'bern', 'milano', 'tor']
currencies = ['nis', 'fra', 'eur', 'cad']

# print([triple_value for triple_value in zip(countries, capitals,currencies)])
print([(a, b, c) for a, b, c in zip(countries, capitals, currencies)])
data1 = [(a, b, c) for a, b, c in zip(countries, capitals, currencies)]
print(f"{data1} LIST OF TUPLES ")
data2 = map(list, data1)
print(f"{[v for v in data2]} now lists ")


def f2(n):
    if 50 < n < 100:
        return True


numbers1 = [12, 12, 123, 231, 21, 45, 2232, 456, 5667, 899, 567, 345, 6567, 89, 90, 4433, -992345]

numbers2 = filter(f2, numbers1)
print([n for n in numbers2])


list = [1,2,3,4,4]
del list
