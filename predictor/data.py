from typing import Optional, NoReturn, Union
from .types import CURRENCY, DATE, PERIOD, DATA, IData
from .interfaces import IDataAccess, IDataExtractor, ExtractorStrategy, Memento, Observer
from .logger import log
from datetime import datetime


class DataMemento(Memento):
    @log(role='Memento (Memento)')
    def __init__(self, state):
        self.__state = state
        self.__date = datetime.now()

    @log(role='Memento (Memento)', method_role='some memento logic')
    def get_date(self):
        return self.__date

    @log(role='Memento (Memento)', method_role='state getter')
    def get_state(self):
        return self.__state


class Data(IData):
    @log(role='Boss (Memento)')
    def __init__(self, data: list):
        self.__state: list = data

    @log(role='Boss (Memento)')
    def slice(self):
        pass

    @log(role='Boss (Memento)')
    def print(self):
        print(self.__state)

    @log(role='Boss (Memento)')
    def save(self):
        pass

    @log(role='Boss (Memento)')
    def extend(self, data):
        self.__state.extend(data)

    @log(role='Boss (Memento)')
    def borders(self):
        pass

    @log(role='Boss (Memento)', method_role='memento getter')
    def get_state(self):
        return DataMemento(self.__state.copy())

    @log(role='Boss (Memento)', method_role='state setter')
    def restore_state(self, memento: DataMemento):
        self.__state = memento.get_state()


class DataVault(IDataAccess):
    @log(role='Real Subject (Proxy)', type_='method')
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                 end_date: Optional[DATE] = None) -> DATA:
        pass


class DataVaultProxy(IDataAccess, Observer):
    @log(role='Observer (Observer)', method_role='do some preparation')
    def update(self, *args, **kwargs):
        self.__check_connection()

    @log(role='Observer (Observer)', method_role='preparation')
    def __check_connection(self):
        if not self.__check_something():
            self.__date = datetime.now()

    @log(role='Observer (Observer)')
    def __init__(self, data_vault):
        self.__data_vault: DataVault = data_vault
        self.__date = datetime.now()

    @log(role='Observer (Observer)')
    def get_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                 end_date: Optional[DATE] = None) -> DATA:

        if self.__check_something():
            return self.__real.get_data(currency, start_date, period, end_date)
        else:
            pass

    @property
    def __real(self):
        return self.__data_vault

    @log(role='Observer (Observer)')
    def __check_something(self):
        return True


class DataExtractor(IDataExtractor, Observer):
    @log(role='Observer (Observer)', method_role='do some preparation')
    def update(self, *args, **kwargs):
        pass

    @log(role='Main class (Strategy)')
    def __init__(self, strategy: ExtractorStrategy):
        self.__strategy = strategy

    @log(role='Main class (Strategy)', method_role='call strategy method')
    def extract_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                     end_date: Optional[DATE] = None):
        return self.__strategy.extract_data(currency, start_date, period, end_date)

    @log(role='Main class (Strategy)', method_role='call strategy method')
    def exchange_rate(self, currency: tuple[CURRENCY, CURRENCY], date_: DATE):
        return self.__strategy.exchange_rate(currency, date_)

    @log(role='Main class (Strategy)', method_role='call strategy method')
    def available_rates(self) -> list[tuple[CURRENCY, CURRENCY]]:
        return self.__strategy.available_rates()

    @log(role='Main class (Strategy)', method_role='setter')
    def set_strategy(self, strategy: ExtractorStrategy):
        self.__strategy = strategy


# noinspection DuplicatedCode
class Strategy1(ExtractorStrategy):
    @log(role='Strategy (Strategy)')
    def extract_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                     end_date: Optional[DATE] = None):
        pass

    @log(role='Strategy (Strategy)')
    def exchange_rate(self, currency: tuple[CURRENCY, CURRENCY], date_: DATE):
        pass

    @log(role='Strategy (Strategy)')
    def available_rates(self) -> list[tuple[CURRENCY, CURRENCY]]:
        pass


# noinspection DuplicatedCode
class Strategy2(ExtractorStrategy):
    @log(role='Strategy (Strategy)')
    def extract_data(self, currency: tuple[CURRENCY, CURRENCY], start_date: DATE, period: PERIOD = 'day',
                     end_date: Optional[DATE] = None):
        pass

    @log(role='Strategy (Strategy)')
    def exchange_rate(self, currency: tuple[CURRENCY, CURRENCY], date_: DATE):
        pass

    @log(role='Strategy (Strategy)')
    def available_rates(self) -> list[tuple[CURRENCY, CURRENCY]]:
        pass


class PredictionVault:
    def save(self) -> NoReturn:
        pass

    def history(self) -> list[DATA]:
        pass

    def get_by_date(self, date_: DATE) -> Union[DATA, None]:
        pass