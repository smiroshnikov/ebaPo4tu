from luminoth import Detector, read_image as ri

EXPECTED_RESULTS = [{'bbox': [331, 395, 793, 1877], 'label': 'person', 'prob': 0.9997},
                    {'bbox': [728, 408, 1090, 1895], 'label': 'person', 'prob': 0.9995},
                    {'bbox': [325, 404, 618, 1304], 'label': 'person', 'prob': 0.9515}
                    ]

QA_test_set = ri('heavy_rain.jpg')

detector = Detector(checkpoint='checkpoint_A1.0.1')
ACTUAL_RESULTS = detector.predict(QA_test_set)
assert ACTUAL_RESULTS == EXPECTED_RESULTS, "RESULTS DO not match ! "
