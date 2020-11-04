from typing import Optional, NoReturn, Union
from .types import DATA, CURRENCY, DATE, PERIOD
from .defs import IDataAccess, IDataExtractor


class Data:
    def slice(self):
        pass

    def save(self):
        pass

    def extend(self, data: DATA):
        pass

    def borders(self):
        pass


class DataVault(IDataAccess):
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                 end_date: Optional[DATE] = None) -> DATA:
        pass


class DataVaultProxy(IDataAccess):
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                 end_date: Optional[DATE] = None) -> DATA:
        pass

    @property
    def __real(self):
        return self.__data_vault


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