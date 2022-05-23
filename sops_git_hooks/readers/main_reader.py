from typing import Dict, Iterable, Union
from sops_git_hooks.base_file_operations import get_file_extension

from sops_git_hooks.readers.base import Converter


class ReaderError(Exception):
    pass


class MainReader:
    def __init__(self):
        self.readers: Dict[str, Converter] = {}

    def register_reader(
        self, converter: Converter, extensions: Union[Iterable[str], str]
    ):
        for extension in extensions:
            self.readers[extension] = converter

    def __getitem__(self, extension: str) -> Converter:
        try:
            return self.readers[extension]
        except KeyError:
            raise ReaderError(f"No reader registered for {extension}")

    def read(self, filename: str):
        extension = get_file_extension(filename=filename)
        reader = self[extension]
        return reader.read(filename=filename)

    def write(self, content: Dict, filename: str):
        extension = get_file_extension(filename=filename)
        reader = self[extension]
        return reader.write(content=content, filename=filename)

