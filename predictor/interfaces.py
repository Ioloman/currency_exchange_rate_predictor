from abc import ABC, abstractmethod
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


class IVisualizer(ABC):
    @abstractmethod
    def show(self, *args, **kwargs) -> NoReturn:
        pass

    def __call__(self, *args, **kwargs) -> NoReturn:
        self.show(*args, **kwargs)


class IPredictor(ABC):
    @abstractmethod
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass

    def __call__(self, *args, **kwargs) -> DATA:
        return self.predict(*args, **kwargs)