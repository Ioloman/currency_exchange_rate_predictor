from .logger import log
from .interfaces import IPredictor, IVisualizer


class Manager:
    @log()
    def __init__(self, predictor: IPredictor, visualizer: IVisualizer):
        self.__predictor = predictor
        self.__visualizer = visualizer

    @log(method_role='delegation')
    def predict(self, *args, **kwargs):
        return self.__predictor.predict(*args, **kwargs)

    @log(method_role='delegation')
    def show(self, *args, **kwargs):
        self.__visualizer.show(*args, **kwargs)