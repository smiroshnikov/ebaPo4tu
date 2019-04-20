from luminoth import Detector, read_image as ri, vis_objects

EXPECTED_RESULTS = [{'bbox': [331, 395, 793, 1877], 'label': 'person', 'prob': 0.9997},
                    {'bbox': [728, 408, 1090, 1895], 'label': 'person', 'prob': 0.9995},
                    {'bbox': [325, 404, 618, 1304], 'label': 'person', 'prob': 0.9515}
                    ]

QA_test_set = ri('heavy_rain.jpg')
# detector = Detector(checkpoint='checkpoint_A1.0.1')
detector = Detector()
ACTUAL_RESULTS = detector.predict(QA_test_set)
assert ACTUAL_RESULTS == EXPECTED_RESULTS, "RESULTS DO not match ! "

print(ACTUAL_RESULTS)
print(type(ACTUAL_RESULTS))
print(len(ACTUAL_RESULTS))

vis_objects(QA_test_set, ACTUAL_RESULTS).save('people.png')

for ob in ACTUAL_RESULTS:
    for key, v in ob.items():
        print(f"{key} is key ,{v} is value")

for ob in ACTUAL_RESULTS:
    print(ob)
    print("next ob ! \n")
