import copy
import datetime
import operator
import sys
from time import sleep

# from luminoth import Detector, read_image as ri
from termcolor import colored

"""
SCRIPT FLOW 

1. GET CHECKPOINT ID 
2. EXECUTE OBJECT DETECTION ON IMAGE (luminoth)
3. CREATE DATA STRUCTURE {execution_time : {[list of luminoth dictionaries ]} } - see EXAMPLE below 
key is time delta , value is luminoth output ( list of dictionaries)  

{datetime.timedelta(0, 1, 345175): 
                [{'bbox': [335, 421, 741, 1912], 
                'label': 'person', 'prob': 1.0}, 
                {'bbox': [735, 423, 1111, 1851], 
                'label': 'person', 'prob': 0.9998}, 
                {'bbox': [496, 375, 860, 1873], 
                'label': 'person', 'prob': 0.9997}, 
                {'bbox': [261, 389, 634, 1430], 
                'label': 'person', 'prob': 0.9914}, 
                {'bbox': [323, 571, 1034, 1529], 
                'label': 'person', 'prob': 0.8083}]}
   
2. GET BASIC TEST CASE LIST (each image has various weather conditions and different amount of various objects)

PERFORM TESTS VERSUS EXPECTED RESULT 
3. PER EACH TEST CASE CHECK EXECUTION TIME 
4. PER EACH TEST CASE CHECK COORDINATES MATCH 
5. PER EACH TEST CASE CHECK LABELS AND PROBABILITY 
6. PROVIDE REPORT - cli / terminal / json  whatever required

"""

BASIC_TESTS_SET = ('heavy_rain.jpg', 'sunny_day.jpg',
                   'dusk_low_light.jpg', 'heavy_traffic_500_pedestrians.jpg',
                   'blizzard_helicopter_2_cats.jpg', 'squirrels_on_road_with_trucks.jpg')

EXPECTED_RESULT_REAL = {datetime.timedelta(0, 1, 346245):
                            [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                             {'bbox': [735, 423, 1111, 1851], 'label': 'person', 'prob': 0.9998},
                             {'bbox': [496, 375, 860, 1873], 'label': 'person', 'prob': 0.9997},
                             {'bbox': [261, 389, 634, 1430], 'label': 'person', 'prob': 0.9914},
                             {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]}

checkpoint_name = sys.argv[1]


def extract_objects(img, checkpoint):
    """

    :param img: image file name
    :param checkpoint: checkpoint ID
    :return: dictionary with {delta : {luminoth list of dictionaries }}
    """

    d = Detector(checkpoint=checkpoint)
    image = ri(img)
    start = datetime.datetime.now()
    p = d.predict(image)
    end = datetime.datetime.now()
    print(p)
    execution_time = end - start
    print(colored("LUMINOTH FINISHED ! ", 'yellow'))
    return {execution_time: p}


def validate_execution_time(actual_result, expected_result, test_case_name):
    """
    method that evaluates if execution time of actual result is different from previous /expected
    execution time
    :param actual_result: actual result
    :param expected_result: expected result
    :param test_case_name: test case name (image name)
    :return: dictionary with TC name and pass/fail
    """
    time_diff = list(actual_result.keys())[0] - list(expected_result.keys())[0]
    try:
        assert list(expected_result.keys())[0] >= list(actual_result.keys())[0], \
            colored(
                f"TEST_CASE runtime measurement  <<{test_case_name}>> FAILED reason : slower runtime {time_diff} then previous runtime !"
                , 'red')
    except AssertionError as e:
        print(e)
        pass_flag = False
    else:
        pass_flag = True
        print(colored(f"TEST_CASE runtime measurement on dataset <<{test_case_name}>> PASSED ", 'green'))

    return {test_case_name: ("validate_execution_time", pass_flag)}


def split_dictionary(dd):
    """
    Utility method that splits luminoth list of dictionaries into two separate lists
    :param dd: dictionary provided
    :return: two lists one list of dictionaries [{label : probability }] , [{bbox : [coordinates]}]
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


def extract_label_prob(list_of_dicts):
    """
    extracts only values of person and prob
    :param list_of_dicts: list of dictionaries
    :return: label (dog, bike , human) and probability
    """
    what_and_prob = []
    for element in list_of_dicts:
        my_getter = operator.itemgetter('label', 'prob')
        what_and_prob.append(my_getter(element))
    return what_and_prob


def clean_and_separate(dictionary):
    """
    Method that separates luminoth output into boxes and labels : probabilities
    :param dictionary:   dictionary
    :return: labels and probabilities tuple
             bboxes tuple

    """
    rd = copy.deepcopy(dictionary)
    tmp_data, boxes_coords = split_dictionary(rd)
    labels_and_prob = extract_label_prob(tmp_data)

    return labels_and_prob, boxes_coords


def is_equal(i1, i2):
    """
    method used to compare results between coordinates and labels in expected vs actual
    :param i1: list or dictionary
    :param i2:  list or dictionary
    :return: boolean as result
    """
    if [e for e in i1 if e] == [v for v in i2]:
        return True
    else:
        return False


def validate_values(actual_results, expected_results, test_case):
    """
    this method validates that object detection and location
    :param actual_results:
    :param expected_results:
    :param test_case: test case name
    :return: dict with {test_case name : pass/fail}
    """
    # Splitting the dictionary into two lists , one with bboxes , and other with labels and probabilities
    ar_lp, ar_bx_list = clean_and_separate(actual_results)
    er_lp, er_bx_list = clean_and_separate(expected_results)

    if is_equal(ar_bx_list, er_bx_list):
        # comparing coordinates
        if is_equal(ar_lp, er_lp):
            # comparing labels and values
            pass_flag = True
            print(colored(f"TEST_CASE value accuracy on dataset  <<{test_case}>> PASSED labels and prob match! ",
                          'green'))
        else:
            pass_flag = False
            print(
                colored(f"TEST_CASE value accuracy on dataset  <<{test_case}>> FAILED  labels and prob DO NOT Match! ",
                        'red'))
    else:
        pass_flag = False
        print(f"TEST_CASE value accuracy on dataset <<{test_case}>> FAILED  box coordinates DO NOT Match! ")
    return {test_case: ("validate coordinated and labels", pass_flag)}


print(colored(f"RUNNING REAL IMAGE EXTRACTION WITH LUMINOTH !", 'red'))
# luminoth_output = extract_objects(BASIC_TESTS_SET[0], checkpoint_name)

# print(luminoth_output)
# this is test run on REAL DATA
# validate_execution_time(luminoth_output, EXPECTED_RESULT_REAL, 'sunny_day_3_people.jpg')
# validate_values(luminoth_output, EXPECTED_RESULT_REAL, 'sunny_day_3_people.jpg')
# print(colored(f"EXECUTION ON REAL file is completed", 'red'))

if __name__ == '__main__':

    for t in range(0, 3):
        print(colored(f"FAKE DATA TESTS WILL START in {3 - t}", 'yellow'))
        sleep(1)

    # THOSE ARE TESTS WITH FAKE DATA
    # region MOCK DATA
    EXPECTED_RESULT_GOOD = {datetime.timedelta(0, 1, 351435):
                                [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                                 {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                            }

    EXPECTED_RESULT_RAIN = {datetime.timedelta(0, 1, 351435):
                                [{'bbox': [335, 421, 741, 1912], 'label': 'dog', 'prob': 1.0},
                                 {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                            }
    EXPECTED_RESULT_SUNNY_DAY = {datetime.timedelta(0, 1, 351435):
                                     [{'bbox': [335, 421, 741, 1912], 'label': 'dog', 'prob': 1.0},
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

    ACTUAL_RESULT_BAD_TIME = {datetime.timedelta(0, 1, 951435):
                                  [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                                   {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                              }

    ACTUAL_RESULT_BAD_COORDINATES = {datetime.timedelta(0, 1, 351435):
                                         [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                                          {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
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

    EXPECTED_RESULT_BIG = {datetime.timedelta(0, 1, 351435):
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

    FAKE_RESULTS_LIST = (ACTUAL_RESULT_ALL_GOOD, ACTUAL_RESULT_BAD_TIME, ACTUAL_RESULT_BAD_LABEL)

    # endregion  -< TH

    for tc in BASIC_TESTS_SET:
        print(colored(
            f"<<====================================EXECUTING TEST SET - {tc}==========================================>>",
            'yellow'))
        for r in FAKE_RESULTS_LIST:
            actual_result = r

            validate_execution_time(actual_result, EXPECTED_RESULT_GOOD, tc)
            validate_values(actual_result, EXPECTED_RESULT_BIG, tc)
