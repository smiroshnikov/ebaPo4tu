l = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 4, 5, 6, 7, 8, 98, 9, 34, 23, -75, -75, 75]


def number_of_occ(l):
    results = {}
    for n in l:
        if n in results:
            results[n] += 1
        else:
            results[n] = 1
    return results


def count_shorter(l):
    results = {}
    for n in l:
        results[n] = l.count(n)
    return results


print(f"{number_of_occ(l)} complexity O(n={len(l)})")
print(f"{count_shorter(l)} complexity O(n={len(l)})")
