from typing import Optional
from .interfaces import IPredictor, IVisualizer
from .types import DATA
from .logger import log


class Predictor1(IPredictor):
    @log(role='delegate')
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass


class Predictor2(IPredictor):
    @log(role='delegate')
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass


class Visualizer1(IVisualizer):
    @log(role='delegate')
    def show(self, *args, **kwargs):
        pass


class Visualizer2(IVisualizer):
    @log(role='delegate')
    def show(self, *args, **kwargs):
        pass


class Analyzer:
    def is_true(self, prediction: DATA) -> bool:
        pass

    def prediction_analysis(self, prediction: DATA):
        pass

    def analyze_precision(self):
        pass
