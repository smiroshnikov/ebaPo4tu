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
import time

known_primes = []


def is_prime(n):
    global known_primes
    temp = int(math.sqrt(n))
    if temp in known_primes:
        prime_flag = False
        # print(f"DEBUG: {temp} already discovered trying number {n}")
    else:
        while temp > 1:
            if n % temp == 0:
                prime_flag = False
                break
            temp -= 1
        else:
            prime_flag = True
            known_primes.append(n)
            # print(f"DEBUG: So far discovered {len(known_primes)} primes ! ")
    if prime_flag:
        return n


with open('prime_numbers.txt', 'w') as f:
    start = time.time()
    rv = "".join("{}\n".format(v) for v in map(is_prime, range(0, 17000000)) if isinstance(v, int))
    f.write(f"{rv} ")
    end = time.time()
    print(end - start)

# debug
