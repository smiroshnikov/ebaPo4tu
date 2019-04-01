import math
import sys

b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b * b - 4.0 * c
d = math.sqrt(discriminant)
print(f"first root is {(-b + d) / 2.0}")
print(f"first root is {(-b - d) / 2.0}")
