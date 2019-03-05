def test(list_of_items):
    for key in list_of_items.keys():
        print(key)


test({'a': 1, 'b': 2, 'c': 3})

elements = [(1, 1), (2, 2), (2, 3), (4, 4), (4, 5)]
for x, y in elements:
    pass

print(f"this is the chosen element")
for element in elements:
    pass
print(f"x:{x}, y:{y}")


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cris = Human(age=14, name='cris')

print(f"human age is {cris.age}, and human name is {cris.name}")


