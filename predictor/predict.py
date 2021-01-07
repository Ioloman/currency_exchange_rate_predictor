from typing import Optional
from .interfaces import IPredictor, IVisualizer, EventManager, Observer
from .types import DATA
from .logger import log


class PredictEventManager(EventManager):
    @log(role='Event Manager (observer)')
    def __init__(self):
        self.__objects: list[Observer] = []

    @log(role='Event Manager (observer)', method_role='attach observer')
    def attach(self, obj: Observer):
        self.__objects.append(obj)

    @log(role='Event Manager (observer)', method_role='detach observer')
    def detach(self, obj: Observer):
        self.__objects.remove(obj)

    @log(role='Event Manager (observer)', method_role='notify observers')
    def notify(self, *args, **kwargs):
        for obj in self.__objects:
            obj.update(*args, **kwargs)


class Predictor(IPredictor, Observer):
    @log(role='Observer (Observer)', method_role='do some preparation')
    def update(self, *args, **kwargs):
        self.__get_ready()

    @log(role='Observer (Observer)', method_role='preparation')
    def __get_ready(self):
        self.array = [0] * 1000

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
