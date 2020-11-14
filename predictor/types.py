from abc import ABC, abstractmethod
from typing import Literal, Union, NoReturn
from datetime import datetime, date
from collections.abc import Iterable


class IData(ABC, Iterable):
    @abstractmethod
    def slice(self, a, b):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def extend(self, data) -> NoReturn:
        pass

    @abstractmethod
    def remove(self, data) -> NoReturn:
        pass

    def is_composite(self) -> bool:
        try:
            self.__getattribute__(f'_{self.__class__.__name__}__children')
        except AttributeError:
            return False
        else:
            return True

    @abstractmethod
    def borders(self):
        pass


PERIOD = Literal['day', 'year', ]
DATE = Union[datetime, date]
CURRENCY = Literal['rub', 'usd', 'eu', ]
DATA = IData

