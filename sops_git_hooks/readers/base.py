from abc import ABC, abstractmethod

from sops_git_hooks.base_file_operations import FileChecker


class Converter(ABC):
    def __init__(self, file_checker: FileChecker = FileChecker()):
        self.file_checker: FileChecker = file_checker

    @abstractmethod
    def write(self, filename):
        ...

    @abstractmethod
    def read(self, filename):
        ...
