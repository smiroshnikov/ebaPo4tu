# example 1 list of functions with same signature
# def diff(a, b): return f"diff = {a - b}"
#
#
# def summ(a, b): return f"sum = {a + b}"
#
#
# def mul(a, b): return f"mul = {a * b}"
#
#
# function_list = [diff, summ, mul]  # function can be called AS AN OBJECT AS WELL !
# print([f(1, 4) for f in function_list])
import math

known_primes = []


def is_prime(n):
    global known_primes
    temp = int(math.sqrt(n))
    if temp in known_primes:
        prime_flag = False
        print(f"{temp} already discovered ")
    else:
        while temp > 1:
            if n % temp == 0:
                prime_flag = False
                break
            temp -= 1
        else:
            prime_flag = True
            known_primes.append(n)
            print(f"So far discovered {len(known_primes)} primes ! ")
    if prime_flag:
        return n


map_result = map(is_prime, range(0, 170000000))
print(f"{[v for v in map_result if isinstance(v, int)]} \n ")

