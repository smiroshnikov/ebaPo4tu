num = 5
print('abc' if num > 0 else 'gaga')

reference_to_object_int = 19 or 1
print(reference_to_object_int)

reference_to_object_float = 0 and 2.5
print(reference_to_object_float)

reference_to_string_object = True and "Evaluate me plz!"
print(reference_to_string_object)

print(not 0 and 24)

letter = 'a'

print(letter in "word")

a = [12, 3, 4]
b = [12, 3, 4]

if a == b:
    print("equal")
elif a is b:
    print("diferent object, expecting same reference  ")

a = (12, 2, 2)
b = (12, 2, 2)

if a is b:
    print("tuples Hold the same reference ! ")

c = 12121212121211212121234234234231
d = 12121212121211212121234234234232
c += 1
if c == d:
    print("same value")
if c is d:
    print("same reference ")

print(12.2 / 2)
print(12.2 // 2)
print(-12.2 // 2)

# chained multiple comparison

if 0 < num < 10:
    print(f"between 0 and 10 ")

# unlimited precicion 
num = 423**91500
print(num)
