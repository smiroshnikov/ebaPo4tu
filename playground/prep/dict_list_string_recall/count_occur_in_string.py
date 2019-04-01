s1 = "oooooooxxoooooo"
s2 = "oxoxooooooooooo"


def count_x_o(s):
    results = {}
    for l in s:
        results[l] = s.count(l)
    return results


print(count_x_o(s1))
print(count_x_o(s2))

