lines = []

with open('cities.csv', 'r') as f:
    for line in f:
        fields = (line.split(','))
        # lines.append(f.readline())
        lines.append(fields)
print([value.strip('\n') for line in lines for value in line])
