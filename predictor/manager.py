from .logger import log
from .interfaces import DataCreator
from copy import copy, deepcopy


class Manager:
    @log()
    def __init__(self, factory: DataCreator):
        self.__factory = factory

    @log(role='Client (Factory method)')
    def use_factory(self, *args):
        data = self.__factory.create_data(*args)
        shallow_copy = copy(data)
        deep_copy = deepcopy(data)
        data.extend(deep_copy)
        data.save()