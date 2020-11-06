from typing import Optional, NoReturn, Union
from .types import CURRENCY, DATE, PERIOD, DATA, IData
from .interfaces import IDataAccess, IDataExtractor
from .logger import log


class Data(IData):
    def slice(self):
        pass

    def save(self):
        pass

    def extend(self, data: DATA):
        pass

    def borders(self):
        pass


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