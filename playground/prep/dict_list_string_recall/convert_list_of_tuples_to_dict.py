list_of_t = [("x", 1), ("y", 0), ("z", 3), ("e", 23), ("w", 2), ("q", 90)]


def convert_list_of_tup_to_dict(l):
    d = {}
    for e in l:
        d[e[0]] = e[1]
    return d


for k, v in convert_list_of_tup_to_dict(list_of_t).items():
    print(f"key -> {k, v} <-value")


