from typing import Optional, NoReturn, Union
from .types import CURRENCY, DATE, PERIOD, DATA, IData
from .interfaces import IDataAccess, IDataExtractor
from .logger import log
from collections.abc import Iterator


class DataIterator(Iterator):
    @log(role='Iterator (Iterator)')
    def __init__(self, collection: list[IData]):
        self.__collection: list[IData] = collection
        self.__index: int = 0
        self.__stack = []
        self.__current: IData = 0

    @log(role='Iterator (Iterator)', method_role='опред. текущего элемента')
    def __next(self):
        if len(self.__collection) > self.__index:
            self.__current = self.__collection[self.__index]
        elif self.__stack:
            self.__collection, self.__index = self.__stack.pop(-1)
            while not len(self.__collection) > self.__index:
                if self.__stack:
                    self.__collection, self.__index = self.__stack.pop(-1)
                else:
                    raise StopIteration()
            else:
                self.__current = self.__collection[self.__index]
        else:
            raise StopIteration()

    @log(role='Iterator (Iterator)', method_role='возврат следующего элемента')
    def __next__(self):
        self.__next()
        while self.__current.is_composite():
            self.__stack.append((self.__collection, self.__index + 1))
            self.__collection = self.__collection[self.__index].collection
            self.__index = 0
            self.__next()
        self.__index += 1

        return self.__current


class DataComposite(IData):
    @log(role='Composite (Composite)')
    def __init__(self, children: list[IData] = []):
        self.__children: list[IData] = children.copy()

    @log(role='Composite (Composite)', method_role='удаление ребенка')
    def remove(self, data: DATA) -> NoReturn:
        self.__children.remove(data)

    @log(role='Composite (Composite)', method_role='срез')
    def slice(self, a, b) -> Union[IData, None]:
        composite = DataComposite()
        for child in self.__children:
            result = child.slice(a, b)
            if result:
                composite.extend(result)
        if len(composite):
            return composite
        else:
            return None

    @log(role='Composite (Composite)', method_role='строковое представление')
    def __str__(self) -> str:
        string = ''
        for child in self.__children:
            string += child.__str__() + ' '
        return ' '.join(string.split())

    @log(role='Composite (Composite)')
    def save(self):
        for child in self.__children:
            child.save()

    @log(role='Composite (Composite)', method_role='добавление ребенка')
    def extend(self, data: DATA) -> NoReturn:
        self.__children.append(data)

    @log(role='Composite (Composite)', method_role='макс. и мин. элементы')
    def borders(self):
        return self.min(), self.max()

    @log(role='Composite (Composite)', method_role='макс. элемент')
    def max(self):
        m = float('-inf')
        for child in self.__children:
            if child.max() > m:
                m = child.max()
        return m

    @log(role='Composite (Composite)', method_role='мин. элемент')
    def min(self):
        m = float('inf')
        for child in self.__children:
            if child.min() < m:
                m = child.min()
        return m

    @log(role='Composite (Composite)', method_role='размер композита')
    def __len__(self):
        return len(self.__children)

    @log(role='Composite (Composite)', method_role='возвращает итератор по коллекции')
    def __iter__(self) -> DataIterator:
        return DataIterator(self.__children)

    @property
    def collection(self):
        return self.__children


class DataLeaf(IData):
    @log(role='Leaf (Composite)')
    def __init__(self, n):
        self.n = n

    def remove(self, data: DATA) -> NoReturn:
        pass

    @log(role='Leaf (Composite)', method_role='срез')
    def slice(self, a, b) -> Union[IData, None]:
        if a < self.n < b:
            return self
        else:
            return None

    @log(role='Leaf (Composite)', method_role='строковое представление')
    def __str__(self) -> str:
        return str(self.n)

    @log(role='Leaf (Composite)')
    def save(self):
        pass

    def extend(self, data: DATA) -> NoReturn:
        pass

    @log(role='Leaf (Composite)', method_role='вместо min() и max(), т.к. элем. один')
    def borders(self):
        return self.n

    def __getattr__(self, item):
        if item == 'min' or item == 'max':
            return self.borders
        else:
            raise AttributeError()

    @log(role='Leaf (Composite)', method_role='возвращает размер (1)')
    def __len__(self):
        return 1

    @log(role='Leaf (Composite)', method_role='возвращает итератор')
    def __iter__(self) -> DataIterator:
        return DataIterator([self])


class DataVault(IDataAccess):
    @log(role='Real Subject (Proxy)', type_='method')
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                 end_date: Optional[DATE] = None) -> DATA:
        pass


class DataVaultProxy(IDataAccess):
    @log(role='Proxy (Proxy)')
    def __init__(self, data_vault):
        self.__data_vault: DataVault = data_vault

    @log(role='Proxy (Proxy)')
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                 end_date: Optional[DATE] = None) -> DATA:

        if self.__check_something():
            return self.__real.get_data(currency, start_date, period, end_date)
        else:
            pass

    @property
    def __real(self):
        return self.__data_vault

    @log(role='Proxy (Proxy)')
    def __check_something(self):
        return True


class DataExtractor(IDataExtractor):
    def extract_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                     end_date: Optional[DATE] = None):
        pass

    def exchange_rate(self, currency: tuple[CURRENCY, CURRENCY], date_: DATE):
        pass

    def available_rates(self) -> list[tuple[CURRENCY, CURRENCY]]:
        pass


class PredictionVault:
    def save(self) -> NoReturn:
        pass

    def history(self) -> list[DATA]:
        pass

    def get_by_date(self, date_: DATE) -> Union[DATA, None]:
        pass