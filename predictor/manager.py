from .logger import log
from .interfaces import IPredictor, IVisualizer, Memento
from .data import DataExtractor, Strategy1, Strategy2, Data, DataVault, DataVaultProxy
from random import choices
from .predict import Predictor, PredictEventManager


class Manager:
    @log(role='client')
    def __init__(self):
        self.__extractor = DataExtractor(Strategy1())
        self.__states: list[Memento] = []
        self.__vault = DataVaultProxy(DataVault())
        self.__predictor = Predictor()
        self.__event_manager = PredictEventManager()


    @log(role='client')
    def extract_data(self, *args, **kwargs):
        if kwargs['source'] == '1':
            self.__extractor.set_strategy(Strategy1())
        elif kwargs['source'] == '2':
            self.__extractor.set_strategy(Strategy2())
        kwargs.pop('source')
        self.__extractor.extract_data(*args, **kwargs)

    @log(role='client')
    def remember_data(self, data: Data):
        self.__states.append(data.get_state())

    @log(role='client')
    def change_data(self, data: Data):
        data.extend(choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=5))

    @log(role='client')
    def restore_state(self, data: Data):
        data.restore_state(self.__states.pop())

    @log(role='client')
    def configure_observers(self):
        self.__event_manager.attach(self.__predictor)
        self.__event_manager.attach(self.__vault)

    @log(role='client')
    def predict_button_pressed(self):
        self.__event_manager.notify()

    @log(role='client')
    def reconfigure_observers(self):
        self.__event_manager.detach(self.__vault)
