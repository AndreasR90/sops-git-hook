from dataclasses import dataclass
from typing import List, Type

from sops_git_hooks.readers.base import Converter
from sops_git_hooks.readers.ini import IniConverter, IniOptions
from sops_git_hooks.readers.json import JsonConverter, JsonOptions
from sops_git_hooks.readers.yaml import YamlConverter, YamlOptions


@dataclass
class ConverterPair:
    converter: Type[Converter]
    converter_options: object
    extensions: List[str]


converters = [
    ConverterPair(
        converter=JsonConverter, converter_options=JsonOptions, extensions=["json"]
    ),
    ConverterPair(
        converter=YamlConverter,
        converter_options=YamlOptions,
        extensions=["yaml", "yml"],
    ),
    ConverterPair(
        converter=IniConverter, converter_options=IniOptions, extensions=["ini"]
    ),
]
