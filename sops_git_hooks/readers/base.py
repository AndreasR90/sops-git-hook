from abc import ABC, abstractmethod


class Converter(ABC):
    @abstractmethod
    def write(self, filename):
        ...

    @abstractmethod
    def read(self, filename):
        ...
