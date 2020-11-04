from logger import log
from abc import ABC, abstractmethod


class Base(ABC):
    role = ABC

    @abstractmethod
    def test(self):
        pass


class Test(Base):
    @log(method_role='role')
    def test(self):
        print('do something')


if __name__ == '__main__':
    test1 = Test()
    test1.test()

