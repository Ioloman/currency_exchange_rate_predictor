from abc import ABC, abstractmethod
from typing import Optional, NoReturn
from .types import CURRENCY, PERIOD, DATE, DATA, IData
from copy import deepcopy
from .logger import log


class SingletonMeta(type):

    __instances = {}

    @log(role='Singleton metaclass (Singleton)', method_role='managing instances')
    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class DataCreator(ABC):
    @staticmethod
    @log(role='Factory base class (Factory method)', class_='DataCreator', type_='staticmethod')
    def copy_data(self, obj: IData) -> IData:
        return deepcopy(obj)

    @abstractmethod
    def create_data(self, *args) -> IData:
        pass


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
        self.__class__.show(*args, **kwargs)


class IPredictor(ABC):
    @abstractmethod
    def predict(self, data_: DATA, n: Optional[int] = None) -> DATA:
        pass

    def __call__(self, *args, **kwargs) -> DATA:
        return self.__class__.predict(*args, **kwargs)