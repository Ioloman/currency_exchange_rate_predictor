from abc import ABC, abstractmethod
from typing import Literal, Union
from datetime import datetime, date


class IData(ABC):
    @abstractmethod
    def slice(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def extend(self, data):
        pass

    @abstractmethod
    def borders(self):
        pass


PERIOD = Literal['day', 'year', ]
DATE = Union[datetime, date]
CURRENCY = Literal['rub', 'usd', 'eu', ]
DATA = IData

