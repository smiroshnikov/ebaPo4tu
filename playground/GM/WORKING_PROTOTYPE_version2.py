import copy
import datetime
import operator
import sys

"""
SCRIPT FLOW SHOULD BE LIKE THIS 

1. GET CHECKPOINT ID 
2. GET TEST CASE LIST (TUPLE OF IMAGES)
3. PER EACH TEST CASE CHECK EXECUTION TIME 
4. PER EACH TEST CASE CHECK COORDINATES MATCH 
5. PER EACH TEST CASE CHECK LABELS AND PROBABILITY 
6. GENERATE REPORT -> {"MODEL/CHECKPOINT_ID" : chk_id , 
                        test : 'rainy_day.jpg' , 
                        'detection' : 'passed',
                        'execution' : 'failed'} 

"""
# region Data Structures


BASIC_TESTS_SET = ('heavy_rain.jpg', 'sunny_day.jpg', 'dusk_low_light.jpg', 'heavy_traffic.jpg', 'blizzard.jpg',
                   'squirrel_on_road.jpg')
checkpoint_name = sys.argv[1]

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

ACTUAL_RESULT_BIG = {datetime.timedelta(0, 1, 351435):
                         [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                          {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                     }

RESULTS_LIST = (ACTUAL_RESULT_ALL_GOOD, ACTUAL_RESULT_BAD_TIME, ACTUAL_RESULT_BAD_LABEL)


# endregion


def do_luminoth(checkpoint):
    print(f"results for checkpoint ID <<{checkpoint}>>")
    return ACTUAL_RESULT_ALL_GOOD


def validate_execution_time(ar, er, tc):
    """

    :param ar:
    :param er:
    :param tc:
    :return:
    """
    time_diff = list(ar.keys())[0] - list(er.keys())[0]
    try:
        assert list(er.keys())[0] >= list(ar.keys())[0], \
            f"TEST_CASE runtime measurement  <<{tc}>> FAILED reason : slower runtime {time_diff} then previous runtime !"
    except AssertionError as e:
        print(e)
        pass_flag = False
    else:
        pass_flag = True
        print(f"TEST_CASE runtime measurement on dataset <<{tc}>> PASSED ")

    return {tc: ("validate_execution_time", pass_flag)}


def split_dictionary(dd):
    """

    :param d:
    :return: two lists
    """
    tmp = None
    lp = labels_and_probs = []
    bc = box_coordinates = []
    for k, v in dd.items():
        tmp = v

    for d in tmp:
        box_coordinates.append(d.pop('bbox'))
        labels_and_probs.append(d)

    # print(f"DEBUG::{labels_and_probs}-> labels_probs ")
    # print(f"DEBUG::{box_coordinates}-> bboxes ")

    return lp, bc


def extract_label_prob(l):
    """
    extracts only values of person and prob as THEY are validated
    :param l: list of dictionaries
    :return:
    """
    what_and_prob = []
    for element in l:
        my_getter = operator.itemgetter('label', 'prob')
        what_and_prob.append(my_getter(element))
    return what_and_prob


def clean_and_separate(result_dictionary):
    """

    :param result_dictionary: Actual Result dictionary
    :param er: Expected Result dictionary
    :return: expected results labels and probabilities tuple
             actual result labels and probabilities
             expected results box coordinates
             actual results box coordinates
    """
    rd = copy.deepcopy(result_dictionary)
    tmp_data, boxes_coords = split_dictionary(rd)

    labels_and_prob = extract_label_prob(tmp_data)

    return labels_and_prob, boxes_coords


def comparator(i1, i2, tc):
    # TODO add an <err> as a failure reason to global ? dictionary - Gulbit
    """
    compares two lists of items for identical entries , value - by - value
    :param i1: list of values
    :param i2: list of values
    :param tc:
    :return:
    """
    try:
        assert [e for e in i1 if e] == [v for v in i2], \
            f"TEST_CASE <<{tc}>> FAILED reason ELEMENT VALIDATION\nelements in\n->{i1}\n do not match elements in \n->{i2}"
    except AssertionError as err:
        print(err)
        test_flag = False
    else:
        test_flag = True
        print(f"TEST_CASE<<{tc}>> PASSED")
    return {tc: test_flag}


def better_comparator(i1, i2):
    if [e for e in i1 if e] == [v for v in i2]:
        return True
    else:
        return False


def validate_values(ar, er, tc):
    ar_lp, ar_bx_list = clean_and_separate(ar)
    er_lp, er_bx_list = clean_and_separate(er)

    if better_comparator(ar_bx_list, er_bx_list):
        if better_comparator(ar_lp, er_lp):
            print(f"TEST_CASE value accuracy on dataset  <<{tc}>> PASSED labels and prob match! ")
        else:
            print(f"TEST_CASE value accuracy on dataset  <<{tc}>> FAILED  labels and prob DO NOT Match! ")
    else:
        print(f"TEST_CASE value accuracy on dataset <<{tc}>> FAILED  box coordinates DO NOT Match! ")


if __name__ == '__main__':
    RESULTS_LIST = (ACTUAL_RESULT_ALL_GOOD, ACTUAL_RESULT_BAD_TIME, ACTUAL_RESULT_BAD_LABEL)
    RM = []

    for tc in BASIC_TESTS_SET:
        for r in RESULTS_LIST:
            actual_result = r
            RM.append(validate_execution_time(actual_result, EXPECTED_RESULT, tc))
            RM.append(validate_values(actual_result, EXPECTED_RESULT, tc))
