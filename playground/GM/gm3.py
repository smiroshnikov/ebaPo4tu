from luminoth import Detector, read_image as ri


class ValidatePerception(object):
    detector = Detector()

    def __init__(self, data_set):
        self.image = data_set

    def get_results(self):
        res = self.detector.predict(self.image)
        return res


vp = ValidatePerception('heavy_rain.jpg')
print(vp.get_results())
