from abc import ABC, abstractmethod, ABCMeta
from typing import Optional, NoReturn
from .types import CURRENCY, PERIOD, DATE, DATA, IData


class IDataAccess(ABC):
    @abstractmethod
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE,
                 period: PERIOD = 'day', end_date: Optional[DATE] = None) -> DATA:
        pass


class IDataExtractor(ABC):
    @abstractmethod
    def extract_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE,
                     period: PERIOD = 'day', end_date: Optional[DATE] = None):
        pass

    @abstractmethod
    def exchange_rate(self, currency: tuple[CURRENCY, CURRENCY], date_: DATE):
        pass

    @abstractmethod
    def available_rates(self) -> list[tuple[CURRENCY, CURRENCY]]:
        pass


class ExtractorStrategy(IDataExtractor, metaclass=ABCMeta):
    pass


class Memento(ABC):
    @abstractmethod
    def get_date(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class EventManager(ABC):
    @abstractmethod
    def attach(self, obj: Observer):
        pass

    @abstractmethod
    def detach(self, obj: Observer):
        pass

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass


class IVisualizer(ABC):
    @abstractmethod
    def show(self, *args, **kwargs) -> NoReturn:
        pass

    def __call__(self, *args, **kwargs) -> NoReturn:
        self.__class__.show(*args, **kwargs)


class IPredictor(ABC):
    @abstractmethod
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass

    def __call__(self, *args, **kwargs) -> DATA:
        return self.__class__.predict(*args, **kwargs)