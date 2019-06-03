class Student:
    def __init__(self, id, name, avg):
        self.avg = avg
        self.name = name
        self.id = id

    def __repr__(self):
        return "id=" + str(self.id) + "name=" + str(self.name) + "avg=" + str(self.avg)


# pure function is filter
students1 = [Student(12, "mish", 88), Student(12, "dish", 81), Student(12, "zish", 18)]
print(students1)
students2 = filter(lambda ob: ob.avg > 80, students1)
print(f"{type(students2)}students2 filter object ")

for s in students2:
    print(s)

# or

students1 = [Student(12, "mish", 88), Student(12, "dish", 81), Student(12, "zish", 18)]
print(students1)
students2 = filter(lambda ob: ob.avg > 80, students1)
stud3 = list(students2)
print(f"{stud3}------------stud3")

data = [(12121123, "daniel", 54),
        (12121123, "ronen", 92),
        (12121123, "moshe", 80),
        (12121123, "yael", 70)]

# higher order function
best_student = lambda dat: max(dat, key=lambda ob: ob[2])
print(best_student(data))


# what is yield


def numbers():
    for num in range(10):
        print(f"num = {num}")
        yield num


for n in numbers():
    pass
    # print(type(n))


def numbers2():
    print("gag lal")
    yield 1
    print("gag lal fafa")
    print("gag lal koko dada")
    print("gag lalza zazazazazazaaaz")
    yield 100
    print("gag lalza zazazazazazaaaz")
    yield 8


for n in numbers2():
    print(n)

# yield return GENERATOR objext - google up lazy evaluation

# Currying Functions
