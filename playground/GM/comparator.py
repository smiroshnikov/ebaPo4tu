import datetime
import operator

EXPECTED_RESULT = {datetime.timedelta(0, 1, 351435):
                       [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                        {'bbox': [735, 423, 1111, 1851], 'label': 'person', 'prob': 0.9998},
                        {'bbox': [496, 375, 860, 1873], 'label': 'person', 'prob': 0.9997},
                        {'bbox': [261, 389, 634, 1430], 'label': 'person', 'prob': 0.9914},
                        {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
                   }

ACTUAL_RESULT = {datetime.timedelta(0, 1, 371435):
                     [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                      {'bbox': [735, 423, 1111, 1851], 'label': 'person', 'prob': 0.9998},
                      {'bbox': [496, 375, 860, 1873], 'label': 'person', 'prob': 0.9997},
                      {'bbox': [261, 389, 634, 1430], 'label': 'person', 'prob': 0.6684},
                      {'bbox': [323, 571, 1034, 1529], 'label': 'bike', 'prob': 0.8084}]
                 }


# assert time: !!!!

def extract(result):
    tmp = None  # result.values()[0]

    rv = []

    for k, v in result.items():
        tmp = v

    for d in tmp:
        d.pop('bbox')
        rv.append(d)

    return rv


expected_result = extract(EXPECTED_RESULT)
actual_result = extract(ACTUAL_RESULT)
# print(expected_result)
# print(actual_result)

# label_and_prob = expected_result[0]
label_and_prob = expected_result

for element in expected_result:
    label_and_prob = element
    my_getter = operator.itemgetter('label', 'prob')
    print(f"my getter is {my_getter(label_and_prob)}")

# my_getter = operator.itemgetter('label', 'prob')
# print(my_getter(label_and_prob))

# for element in list(ACTUAL_RESULT.values()):
#     print(element)

TEST_RESULT = {'FAILED': {'bbox': [261, 389, 634, 1430], 'label': 'person', 'prob': 0.6684},
               'FAILED': {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}}
