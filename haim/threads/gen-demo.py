def numbers_source():
    values = [21, 22, 23, 45, 67, 87]
    for e in values:
        yield e


def check1(source):
    for num in source:
        if num % 2 == 0:
            yield num


