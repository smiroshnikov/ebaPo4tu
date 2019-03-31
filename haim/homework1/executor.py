from haim.homework1.lib import multiply_2_numbers as m2n


# import inspect


def main():
    print(f"multiplication result is {m2n(2, 4)}")
    print(f"multiplication result is {m2n(12, 0)}")
    print(f"multiplication result is {m2n(-1.5, 4.21)}")
    # print(inspect.getmembers(m2n(1, 4)))

    sequence = [1, 2, 3, 4]
    var_a, *var_b = sequence
    print(var_a)
    print(var_b)


if __name__ == "__main__":
    main()
