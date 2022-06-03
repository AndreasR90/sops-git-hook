from abc import ABC, abstractmethod
from typing import Any

from sops_git_hooks.base_file_operations import FileChecker


class Converter(ABC):
    def __init__(self, file_checker: FileChecker = FileChecker(), options: Any = None):
        self.config = options
        self.file_checker: FileChecker = file_checker

    @abstractmethod
    def write(self, filename):
        ...

    @abstractmethod
    def read(self, filename):
        ...

    @abstractmethod
    def format(self, string) -> str:
        ...
