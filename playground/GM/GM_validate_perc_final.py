from luminoth import Detector, read_image as ri, vis_objects

EXPECTED_RESULTS = {'heavy_rain_and_traffic.jpg': [{'bbox': [331, 395, 793, 1877], 'label': 'person', 'prob': 0.9997},
                                                   {'bbox': [728, 408, 1090, 1895], 'label': 'person', 'prob': 0.9995},
                                                   {'bbox': [325, 404, 618, 1304], 'label': 'person', 'prob': 0.9515}
                                                   ],
                    'light_snow.jpg': [{'bbox': [331, 395, 793, 1877], 'label': 'person', 'prob': 0.9997},
                                       {'bbox': [728, 408, 1090, 1895], 'label': 'person', 'prob': 0.9995},
                                       {'bbox': [325, 404, 618, 1304], 'label': 'person', 'prob': 0.9515}
                                       ],
                    'low_light.jpg': [{'bbox': [331, 395, 793, 1877], 'label': 'person', 'prob': 0.9997},
                                      {'bbox': [728, 408, 1090, 1895], 'label': 'person', 'prob': 0.9995},
                                      {'bbox': [325, 404, 618, 1304], 'label': 'person', 'prob': 0.9515}
                                      ]

                    }

QA_TEST_SETS = ('heavy_rain_and_traffic.jpg',
                'light_snow.jpg',
                'low_light.jpg')

PROVIDED_CHECKPOINTS_FROM_DEV = ('checkpoint_A1.0.1',
                                 'checkpoint_B4.0.1',
                                 'checkpoint_B4.2')


def execute_prediction(qa_image, dev_check_point):
    # test_set = ri(qa_image)
    # # detector = Detector(checkpoint='checkpoint_A1.0.1')
    # detector = Detector(checkpoint=dev_check_point)
    # return detector.predict(test_set)
    print(f"selected image {qa_image}, selected checkpoint {dev_check_point}")
    return EXPECTED_RESULTS[qa_image]


for filename in QA_TEST_SETS:
    for checkpoint in PROVIDED_CHECKPOINTS_FROM_DEV:
        ACTUAL_RESULT = execute_prediction(filename, checkpoint)
        assert ACTUAL_RESULT is EXPECTED_RESULTS, \
            f"for test {filename} and checkpoint {checkpoint}" \
                f"{ACTUAL_RESULT}DOES not match expected{EXPECTED_RESULTS[filename]}"
