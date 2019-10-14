def n():
    # return [21,22,23,45,67,87]

    yield 213
    yield 452
    yield 0
    yield 2
    yield 120
    yield -35


def food():
    values = [21, 22, 23, 45, 67, 87]
    for e in values:
        print("krembo")
        print("bisli")
        print("pizza")
        print("ice cream")
        yield e


ob = food()
print(type(ob))
for i in ob:
    print(i)
