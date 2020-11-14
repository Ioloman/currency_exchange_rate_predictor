from typing import Optional, NoReturn
from .interfaces import IPredictor, IVisualizer
from .types import DATA
from .logger import log
from super_prediction_module import SuperPredict


class SuperPredictAdapter(IPredictor, SuperPredict):
    @log(role='Adapter (Adapter)', method_role='маскирует различия')
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        # -----------------
        # translate data
        # -------------------
        result = self.make_assumption(self.extrapolate_data(data_))
        # ------------------
        # translate result
        # -----------------
        return result


class Predictor1(IPredictor):
    @log(role='delegate')
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass


class Predictor2(IPredictor):
    @log(role='delegate')
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass


class VisualizerDecorator(IVisualizer):
    @log(role='Base Decorator (Decorator)')
    def __init__(self, component: IVisualizer):
        self.__component = component

    @property
    def component(self):
        return self.__component

    @log(role='Base Decorator (Decorator)', method_role='делегирует вызов')
    def show(self, *args, **kwargs) -> NoReturn:
        self.component.show(*args, **kwargs)


class Visualizer1(VisualizerDecorator):
    @log(role='Decorator (Decorator)', method_role='добавляет функциональности')
    def show(self, *args, **kwargs):
        self.__some_pre_action1(*args, **kwargs)
        self.component.show(*args, **kwargs)
        self.__some_post_action1(*args, **kwargs)

    @log(role='Decorator (Decorator)', method_role='действие до основного метода')
    def __some_pre_action1(self, *args, **kwargs):
        pass

    @log(role='Decorator (Decorator)', method_role='действие после основного метода')
    def __some_post_action1(self, *args, **kwargs):
        pass


class Visualizer2(VisualizerDecorator):
    @log(role='Decorator (Decorator)', method_role='добавляет функциональности')
    def show(self, *args, **kwargs):
        self.__some_pre_action2(*args, **kwargs)
        self.component.show(*args, **kwargs)
        self.__some_post_action2(*args, **kwargs)

    @log(role='Decorator (Decorator)', method_role='действие до основного метода')
    def __some_pre_action2(self, *args, **kwargs):
        pass

    @log(role='Decorator (Decorator)', method_role='действие после основного метода')
    def __some_post_action2(self, *args, **kwargs):
        pass


class BaseVisualizer(IVisualizer):
    @log(role='Decorated class (Decorator)', method_role='делает базовый вывод')
    def show(self, *args, **kwargs) -> NoReturn:
        pass


class EmptyVisualizer(IVisualizer):
    @log(role='Decorated class (Decorator)', method_role='ничего не делает')
    def show(self, *args, **kwargs) -> NoReturn:
        pass


class Analyzer:
    def is_true(self, prediction: DATA) -> bool:
        pass

    def prediction_analysis(self, prediction: DATA):
        pass

    def analyze_precision(self):
        pass
