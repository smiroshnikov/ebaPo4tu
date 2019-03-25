def is_prime(n):
    # n = int(input("give me a number "))
    x = int(n / 2)
    while x > 2:
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


#
# numbers_list = [x for x in range(1, 100000)]
# r_list = map(is_prime, numbers_list)
# r_set = set
# print(f"{[v for v in set(r_list) if isinstance(v, int)]} list \n total prime numbers ")


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

firstnames = ["moshe", "dudu", "daniela"]
lastnames = ["israeli", "michael", "darky"]

full_names = zip(firstnames, lastnames)

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

list_of_averages = [student[3] for student in students if student[3] > 80x`]

print(list_of_averages)
