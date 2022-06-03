import configparser
from dataclasses import dataclass
from typing import Dict
from sops_git_hooks.base_file_operations import load_file
from sops_git_hooks.readers.base import Converter


@dataclass
class IniOptions:
    pass


class IniConverter(Converter):
    def __init__(self, options: IniOptions = IniOptions()):
        self.options = options

    def read(self, filename: str) -> Dict:
        plain_text = load_file(filename=filename)
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read_string(plain_text)
        return {s: dict(config.items(s)) for s in config.sections()}

    def write(
        self,
        content: Dict,
        filename: str,
    ) -> None:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read_dict(content)
        with open(filename, "w") as file:
            config.write(file)
