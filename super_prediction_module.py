from predictor.logger import log
from random import choice


class SuperPredict:
    @log(role='Independent class (Adapter)')
    def extrapolate_data(self, data):
        pass

    @log(role='Independent class (Adapter)')
    def make_assumption(self, extrapolation_result):
        pass
