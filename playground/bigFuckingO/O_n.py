def print_first_item():
    # O(1)
    # print(f"This function runs O(1) time, constant time ")
    # print(f"It is not important what item is chosen from list it can lbe list[1] or list[138792341] ")
    L = items[0]


def print_all_items():
    # here it is a O(n), where n is a number of elements in list
    # linear time . where nn is the number of items in the list
    for item in items:
        L = item


def print_all_possible_ordered_pairs():
    for first_item in items:
        for second_item in items:
            L = [first_item,second_item]
            # print(first_item, second_item)


def test():
    """Stupid test function"""
    L = [i for i in range(100)]


if __name__ == '__main__':
    import timeit

    items = [1, 2, 3, 4, 5]
    # print(timeit.timeit("test()", setup="from __main__ import test"))
    print(f' time required to run O(1)  '
          f' {timeit.timeit("print_first_item()",setup="from __main__ import print_first_item")}')
    print(f' time required to run O(n)   '
          f'{timeit.timeit("print_all_items()", setup="from __main__ import print_all_items")}')
    print(f' time required to run O(n^2) '
          f'{timeit.timeit("print_all_possible_ordered_pairs()", setup="from __main__ import print_all_possible_ordered_pairs")}')

