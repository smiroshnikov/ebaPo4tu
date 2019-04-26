import json

# this should be in a file not in test code
luminoth_output = [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                   {'bbox': [735, 423, 1111, 1851], 'label': 'person', 'prob': 0.9998},
                   {'bbox': [496, 375, 860, 1873], 'label': 'person', 'prob': 0.9997},
                   {'bbox': [261, 389, 634, 1430], 'label': 'person', 'prob': 0.9914},
                   {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]

expected_output = [{'bbox': [335, 421, 741, 1912], 'label': 'dog', 'prob': 1.0},
                   {'bbox': [735, 423, 1111, 1851], 'label': 'bike', 'prob': 0.9998},
                   {'bbox': [496, 375, 860, 1873], 'label': 'car', 'prob': 0.9997},
                   {'bbox': [261, 389, 634, 1430], 'label': 'plane', 'prob': 0.9914},
                   {'bbox': [323, 571, 1034, 1529], 'label': 'gorilla', 'prob': 0.8083}]


# result_i_need = '{"bbox": [335, 421, 741, 1912], "label": "person", "prob": "1.0"}'

def luminoth_2_str(luminoth_obj):
    """
    converts a luminoth output list of dicts to list of strings
    that can be used as serialized json object
    :param luminoth_obj:
    :return: list of strings
    """
    ls = [str(i).replace("'", '"') for i in luminoth_obj]
    return ls


class Serialize2Json(object):
    """
    Converts string to json object
    """

    def __init__(self, j):
        self.__dict__ = json.loads(j)


# example of "easy" usage

actual_result = luminoth_2_str(luminoth_output)
expected_result = luminoth_2_str(expected_output)

for a_line in actual_result:
    actual_content = Serialize2Json(a_line)
    for e_line in expected_result:
        expected_content = Serialize2Json(e_line)
        # here comparison can be done for  values,
        # probability , and object location
        # with fancy colors and all that
        print(f"actual coordinates -> <<{actual_content.bbox}>>\n "
              f"expected coordinates -><<{expected_content.bbox}>>\n")
        print(f"current label is -> <<{actual_content.label}>> , expected label was <<{expected_content.label}>> ")
        # and so on . my script should be much shorter
