import datetime
import operator


# TODO add comments make this a utility class

def clean_and_separate_v2(result_dictionary):
    """

    :param result_dictionary: Actual Result dictionary
    :param er: Expected Result dictionary
    :return: expected results labels and probabilities tuple
             actual result labels and probabilities
             expected results box coordinates
             actual results box coordinates
    """

    def split_dictionary(d):
        """

        :param d:
        :return: two lists
        """

        lp = labels_and_probs = []
        bc = box_coordinates = []
        for k, v in d.items():
            tmp = v

        for d in tmp:
            box_coordinates.append(d.pop('bbox'))
            labels_and_probs.append(d)

        # print(f"{labels_and_probs}-> data ")
        # print(f"{box_coordinates}-> bboxes ")

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
            # print(f"element is {my_getter(element)}")
            what_and_prob.append(my_getter(element))
        return what_and_prob

    tmp_data, boxes_coords = split_dictionary(result_dictionary)
    # er_tmp_data, er_boxes = split_dictionary(er)
    # er_labels_and_prob = extract_label_prob(er_tmp_data)
    labels_and_prob = extract_label_prob(tmp_data)

    return labels_and_prob, boxes_coords


ar = {datetime.timedelta(0, 1, 351435):
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

er = {datetime.timedelta(0, 1, 351435):
          [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
           {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
      }

ar_labels_prob, ar_boxes = clean_and_separate_v2(ar)
er_labels_prob, er_boxes = clean_and_separate_v2(er)
print(ar_labels_prob)
print("===============")
print(ar_boxes)
print("===============")
print(er_labels_prob)
print("===============")
print(er_boxes)
