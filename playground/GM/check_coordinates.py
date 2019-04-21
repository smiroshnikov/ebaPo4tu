BASIC_TESTS_SET = ('heavy_rain.jpg', 'sunny_day.jpg', 'dusk_low_light.jpg')

l_p_actual = [('person', 1.0), ('person', 1.0),
              ('person', 1.0), ('person', 1.0),
              ('dog', 0.8083)]

l_p_expected = [('person', 1.0), ('person', 1.0),
                ('person', 1.0), ('person', 1.0),
                ('person', 0.8083)]

b_c_actual = [[335, 421, 741, 1912],
              [335, 421, 741, 1912],
              [335, 421, 741, 1912],
              [335, 421, 741, 1912],
              [335, 421, 741, 1912],
              [335, 421, 741, 1912]]

b_c_expected = [[335, 421, 741, 1912],
                [335, 421, 741, 1912],
                [335, 421, 741, 1912],
                [335, 421, 741, 1912],
                [335, 421, 741, 1912],
                [335, 421, 741, 1913]]


def validate_values(i1, i2, tc):
    # TODO add an <err> as a failure reason to global ? dictionary - Gulbit
    """

    :param i1:
    :param i2:
    :param tc:
    :return:
    """
    try:
        assert [e for e in i1 if e] == [v for v in i2], \
            f"elements in \n->{i1}\n do not match to elements in \n->{i2} "
    except AssertionError as err:
        print(err)
        test_flag = False
    else:
        test_flag = True
    return {tc: test_flag}


r1 = validate_values(b_c_actual, b_c_expected, 'fff.jpg')

print(r1)
