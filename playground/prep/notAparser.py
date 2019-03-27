lines = []

with open('cities.csv', 'r') as f:
    for line in f:
        # fields = (line.split(','))
        fields = (line)
        # lines.append(f.readline())
        lines.append(fields)

print([l for l in lines])
print(f"{len(lines)}")
# print([value.strip('\n') for line in lines for value in line])



class Foo:
    def __call__(self, *args, **kwargs):
        print("called")


foo_instance = Foo()
foo_instance()
