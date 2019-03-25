# augmented assignment


seq = [1, 2, 3, 4]
*var_a, var_b = seq
print(*var_a)

a, b, c, d = 1, 2, 3, 5
print(a, b, c, d, sep='qqq', end=' \n')


def swapa_vs_b(a=3, b=4):
    print(f"before swap a is {a}, b is {b}", sep=' ', end='\n')
    a, b = b, a
    print(f"a is {a}")
    print(f"b is {b}")


swapa_vs_b()
swapa_vs_b(12, 45)

# printing in an ugly and stupid old fashioned type way
print("a=%d b=%d c=%d s=%s " % (12, 23, 45, "old way !"))


def while_mutip(final=10):
    result = 1

    while final != 0:
        result *= final
        final -= 1
        print(f"result is {result} and final is {final}")


print("=====================================")
while_mutip(10)

while True:
    if True:
        print("Oh no break !")
        break
