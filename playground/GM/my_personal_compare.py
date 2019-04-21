import datetime
import operator

# region Data Structures

TC = ('sunny_day.jpg', 'rainy_day.jpg')

EXPECTED_RESULT = {datetime.timedelta(0, 1, 351435):
                       [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                        {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                   }

ACTUAL_RESULT_ALL_GOOD = {datetime.timedelta(0, 1, 351435):
                              [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                               {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                          }

ACTUAL_RESULT_BAD_LABEL = {datetime.timedelta(0, 1, 351435):
                               [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                                {'bbox': [323, 571, 1034, 1529], 'label': 'bike', 'prob': 0.8084}]
                           }
ACTUAL_RESULT_BAD_PROB = {datetime.timedelta(0, 1, 351435):
                              [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                               {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.3084}]
                          }

ACTUAL_RESULT_BAD_TIME = {datetime.timedelta(0, 1, 771435):
                              [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                               {'bbox': [323, 571, 1034, 1529], 'label': 'bike', 'prob': 0.8084}]
                          }


# endregion


def do_luminoth(checkpoint):
    print(f"results for {checkpoint}")
    return ACTUAL_RESULT_ALL_GOOD


def validate_execution_time(ar, er, tc):
    try:
        assert list(er.keys())[0] >= list(ar.keys())[0], \
            f"Actual runtime for {tc}is slower by {list(ar.keys())[0] - list(er.keys())[0]} than previous runtime !"
    except AssertionError as e:
        print(f"TEST_CASE {tc} FAILED ")
        print(e)
        pass_flag = False
    else:
        pass_flag = True
        print(f"TEST_CASE {tc} PASSED ")

    return {tc: ("validate_execution_time", pass_flag)}


# works !


def validate_content_plain_comparison(ar, er):
    assert [av for av in ar.values() if av] == [ev for ev in er.values()], "values do not match "


def remove_bboxes_from_results(result):
    tmp = None
    rv = []

    for k, v in result.items():
        tmp = v

    for d in tmp:
        d.pop('bbox')
        rv.append(d)

    return rv


def validate_object_content(ar=None, er=None):
    ar = {datetime.timedelta(0, 1, 351435):
              [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
               {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
          }
    er = ar

    for k, v in ar.items():
        tmp = v
    

    for element in er:
        label_and_prob = element
        my_getter = operator.itemgetter('label', 'prob')
        print(f"my getter is {my_getter(label_and_prob)} and its type is {type(my_getter(label_and_prob))}")


validate_object_content(ACTUAL_RESULT_ALL_GOOD, EXPECTED_RESULT)

# region Working Code

# RESULTS_MATRIX = []
# RESULTS_MATRIX.append(validate_execution_time(ACTUAL_RESULT_ALL_GOOD, EXPECTED_RESULT, TC[0]))
# RESULTS_MATRIX.append(validate_execution_time(ACTUAL_RESULT_ALL_GOOD, EXPECTED_RESULT, TC[1]))
# RESULTS_MATRIX.append(validate_execution_time(ACTUAL_RESULT_BAD_TIME, EXPECTED_RESULT, TC[1]))
#
# for r in RESULTS_MATRIX:
#     print(r)

# endregion
