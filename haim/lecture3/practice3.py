import fractions

a = 3
b = 4

print("hello" if b > a else "salam")
print('haifa' if b > a and b > 0 else 'ramat gan')
print(109 if a > b else "rehovot")
print("tel aviv" if 'a' in 'abcd' else 'noope')
print('blue ' if 'b' not in "moish" else "red")
print('winter ' if a > 2 and a % 2 == 1 else "summer")
print(123 if 'y' not in 'yahoo' else 'x')

a = fractions.Fraction(3, 4)
b = fractions.Fraction(3, 4)
c = fractions.Fraction(6, 8)
d = a

print(a is b)
print(a is d)
print(a == b)
print(a == c)
print(d is not a)
print(a < b)

a = {1, 2, 3}
b = {2, 3, 4}

print((a | b))  # union
print((a & b))  # bitwise XOR set symmetric difference
print((a ^ b))  # bitwise AND, Set intersection
print((a - b))  # bitwise subtraction, set difference

a = [1, 2, 3]
b = [5, 6, 7]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a * 2)
print(b * 3)
print(71 / 5)
print(71 // 5)
print(2 ** 3)
print(4 ** 2)
print(a[1])
print(b[2])
print(a[0])
print(c[2:7])

a = 12
b = 24
c = 7

print(c < a < b)
print(a < b < c)
print(c < a < b)

num = (a +
       b +
       c +
       d)

ob = a, b, c = 'aaa', 'bbb', 'ccc'
[a, b, c] = [1, 2, 3]

text = "fuck"
[a, b, c, d] = text

print("part 2 ")

[a, b, *c] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a, b)
print(c)
a = b = c = 'xyz'

