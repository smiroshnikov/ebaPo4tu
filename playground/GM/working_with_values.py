import datetime
import operator


# TODO add comments

def clean_and_separate(ar=None, er=None):
    ar = {datetime.timedelta(0, 1, 351435):
              [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
               {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
          }

    er = {datetime.timedelta(0, 1, 351435):
              [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
               {'bbox': [323, 571, 1034, 1529], 'label': 'person', 'prob': 0.8083}]
          }

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

    ar_data, ar_boxes = split_dictionary(ar)
    er_data, er_boxes = split_dictionary(er)

    print(er_boxes)
    print(er_data)

    for element in er_data:
        my_getter = operator.itemgetter('label', 'prob')
        print(f"my getter is {my_getter(element)}")


clean_and_separate()
