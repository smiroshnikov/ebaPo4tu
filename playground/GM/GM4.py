import json
import sys

import datetime

from luminoth import Detector, read_image

BASIC_TESTS_SET = ('heavy_rain.jpg', 'sunny_day.jpg', 'dusk_low_light.jpg')
checkpoint_name = sys.argv[1]


def validate_perception(img):
    d = Detector(checkpoint=checkpoint_name)
    image = read_image(img)
    start = datetime.datetime.now()
    p = d.predict(image)
    end = datetime.datetime.now()
    print(p)
    execution_time = end - start
    return {execution_time: p}


ACTUAL_RESULTS = validate_perception(BASIC_TESTS_SET[0])
EXPECTED_RESULTS = {datetime.timedelta(0, 1, 351435): [{'bbox': [335, 421, 741, 1912], 'label': 'person', 'prob': 1.0},
                                                       {'bbox': [735, 423, 1111, 1851], 'label': 'person',
                                                        'prob': 0.9998},
                                                       {'bbox': [496, 375, 860, 1873], 'label': 'person',
                                                        'prob': 0.9997},
                                                       {'bbox': [261, 389, 634, 1430], 'label': 'person',
                                                        'prob': 0.9914},
                                                       {'bbox': [323, 571, 1034, 1529], 'label': 'person',
                                                        'prob': 0.8083}]}

print([v for v in ACTUAL_RESULTS.values() if v] == [e for e in EXPECTED_RESULTS.values()])
assert [v for v in ACTUAL_RESULTS.values() if v] == [e for e in EXPECTED_RESULTS.values()], "values do not match "

assert list(EXPECTED_RESULTS.keys())[0] >= list(ACTUAL_RESULTS.keys())[0], f"current  execution time\n {list(ACTUAL_RESULTS.keys())[0]}\n " \
    f"is expected to be same or less than previous run \n {list(EXPECTED_RESULTS.keys())[0]}"

# assert EXPECTED_RESULTS[1] == ACTUAL_RESULTS[1], f"\n{EXPECTED_RESULTS} \ndoes not match \n{ACTUAL_RESULTS}\n"

# for test in BASIC_TESTS_SET:
#     detector = Detector(checkpoint=checkpoint_name)
#     img = ri(test)
#     objects = detector.predict(img)
#     for ob in objects:
#         print(f"{test} and result{ob}")
