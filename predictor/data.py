from typing import Optional, NoReturn, Union
from .types import CURRENCY, DATE, PERIOD, DATA, IData
from .interfaces import IDataAccess, IDataExtractor, DataCreator, SingletonMeta, DataFactory
from .logger import log
from copy import deepcopy, copy


class DataPrediction(IData):
    @log(role='Prototype', method_role='shallow copy')
    def __copy__(self):
        return self.__class__(copy(self.custom_prediction_args))

    @log(role='Prototype', method_role='deep copy')
    def __deepcopy__(self, memodict={}):
        return self.__class__(deepcopy(self.custom_prediction_args))

    @log(role='Created by factory (Factory method/Abstract factory)')
    def __init__(self, *args):
        self.custom_prediction_args = args

    @log(role='Created by factory (Factory method/Abstract factory)')
    def slice(self):
        pass

    @log(role='Created by factory (Factory method/Abstract factory)')
    def save(self):
        pass

    @log(role='Created by factory (Factory method/Abstract factory)')
    def extend(self, data: DATA):
        pass

    @log(role='Created by factory (Factory method/Abstract factory)')
    def borders(self):
        pass


class DataHistory(IData):
    @log(role='Prototype', method_role='shallow copy')
    def __copy__(self):
        return self.__class__(copy(self.custom_history_args))

    @log(role='Prototype', method_role='deep copy')
    def __deepcopy__(self, memodict={}):
        return self.__class__(deepcopy(self.custom_history_args))

    @log(role='Created by factory (Factory method/Abstract factory)')
    def __init__(self, *args):
        self.custom_history_args = args

    @log(role='Created by factory (Factory method/Abstract factory)')
    def slice(self):
        pass

    @log(role='Created by factory (Factory method/Abstract factory)')
    def save(self):
        pass

    @log(role='Created by factory (Factory method/Abstract factory)')
    def extend(self, data: DATA):
        pass

    @log(role='Created by factory (Factory method/Abstract factory)')
    def borders(self):
        pass


class MacDataPrediction(DataPrediction):
    pass


class MacDataHistory(DataHistory):
    pass


class MacDataFactory(DataFactory):
    @log(role='Factory (Abstract factory)', method_role='factory initiation')
    def __init__(self):
        pass

    @log(role='Factory (Abstract factory)', method_role='create history data')
    def create_history_data(self, *args) -> IData:
        return MacDataHistory(*args)

    @log(role='Factory (Abstract factory)', method_role='create prediction data')
    def create_prediction_data(self, *args) -> IData:
        return MacDataPrediction(*args)


class WindowsDataFactory(DataFactory):
    @log(role='Factory (Abstract factory)', method_role='factory initiation')
    def __init__(self):
        pass

    @log(role='Factory (Abstract factory)', method_role='create history data')
    def create_history_data(self, *args) -> IData:
        return DataHistory(*args)

    @log(role='Factory (Abstract factory)', method_role='create prediction data')
    def create_prediction_data(self, *args) -> IData:
        return DataPrediction(*args)


class DataPredictionCreator(DataCreator):
    @log(role='Prediction factory (Factory method)', method_role='creates concrete object')
    def create_data(self, *args) -> IData:
        return DataPrediction(*args)


class DataHistoryCreator(DataCreator):
    @log(role='History factory (Factory method)', method_role='creates concrete object')
    def create_data(self, *args) -> IData:
        return DataHistory(*args)


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


class PredictionVault(metaclass=SingletonMeta):
    @log(role='Singleton itself (Singleton)')
    def __init__(self, data):
        self.data = data

    @log(role='Singleton itself (Singleton)')
    def save(self) -> NoReturn:
        pass

    @log(role='Singleton itself (Singleton)')
    def history(self) -> list[DATA]:
        pass

    @log(role='Singleton itself (Singleton)')
    def get_by_date(self, date_: DATE) -> Union[DATA, None]:
        pass