def is_prime(n):
    # n = int(input("give me a number "))
    x = int(n / 2)
    while x > 1:
        if n % x == 0:
            print(f"{n} divides by {x}")
            prime_flag = False
            break
        x -= 1
    else:
        print(f"{n} is prime")
        prime_flag = True

    if prime_flag:
        return n


numbers_list = [x for x in range(1, 1700000)]
r_list = map(is_prime, numbers_list)
print(f"{[v for v in set(r_list) if isinstance(v, int)]} list \n total prime numbers ")


def tuple_swap(t1):
    t1[0], t1[1] = t1[1], t1[0]
    return t1


print(tuple_swap([1, 2]))

l = [1, 2, 3, 4, 5, 6, 7]


def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)


factorials = map(f, l)
print([v for v in map(f, l)])

first_names = ["moshe", "dudu", "daniela"]
last_names = ["israeli", "michael", "darky"]

full_names = zip(first_names, last_names)

for fn in full_names:
    print(fn)

numbers = [12, 3, 1, 0, -34, -2, -3, 87, 10]


def pos(n):
    if n > 0:
        return True
    else:
        return False


print([v for v in filter(pos, numbers)])

students = [("name1", "family1", "121212", 80),
            ("name2", "family2", "1212312", 70),
            ("name3", "family3", "5545412", 90),
            ("name4", "family4", "7001212", 100)]
list_of_averages = [student[3] for student in students if student[3] > 80]
print(list_of_averages)


def diff(a, b): return a - b


def sum(a, b): return a + b


def mul(a, b): return a * b


func_list = [diff, sum, mul]
for f in func_list:
    print(f"{f(21, 2)} amazing")
avg = 90

if avg < 10:
    def calc(mark):
        return mark + 20
else:
    def calc(mark):
        return mark + 10

marks1 = [70, 45, 90]
marks2 = [calc(m) for m in marks1]  # actually will evaluate during runtime
print(marks2)


def avg(grade_list):
    summ = 0
    # sum += [v for v in grade_list] will not work due to LIST COMPREHENSION returning a LIST ! Always
    for k, v in grade_list.items():
        summ += grade_list.get(k)
    return summ / 4


print(avg({'c': 100, 'm': 90, 'p': 87, 'n': 17}))


def diff(a, b): return F"{a - b} this is diff!"


def sum(a, b): return f"{a + b} this is sum!"


def mul(a, b): return f"{a * b} this is mult!"


func_list = [diff, sum, mul]
for f in func_list:
    print(f"{f(21, 2)} amazing")



