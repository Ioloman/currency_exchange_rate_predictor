from .logger import log
from .interfaces import DataCreator, DataFactory
from .types import IData
from copy import copy, deepcopy
from typing import Union


class Manager:
    @log()
    def __init__(self, factory: Union[DataCreator, DataFactory]):
        self.__factory = factory

    @log(role='Client (Factory method)')
    def use_factory(self, *args):
        data = self.__factory.create_data(*args)
        self.use_object(data)

    @log(role='Client (Factory method)')
    def use_object(self, data: IData):
        shallow_copy = copy(data)
        deep_copy = deepcopy(data)
        data.extend(deep_copy)
        data.save()

    @log(role='Client (Abstract factory)')
    def use_abs_factory(self, *args):
        data = self.__factory.create_history_data(*args)
        self.use_object(data)

        data = self.__factory.create_prediction_data(*args)
        self.use_object(data)