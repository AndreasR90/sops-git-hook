from dataclasses import dataclass
from typing import Dict
from sops_git_hooks.base_file_operations import FileChecker
from sops_git_hooks.readers.base import Converter
import yaml


@dataclass
class YamlOptions:
    sort_keys = False


class YamlConverter(Converter):
    def __init__(
        self,
        options: YamlOptions = YamlOptions(),
        file_checker: FileChecker = FileChecker(),
    ):

        self.options = options
        super().__init__(file_checker=file_checker, options=options)

    def read(self, filename: str) -> Dict:
        plain_text = self.file_checker.load_file(filename=filename)
        return yaml.safe_load(plain_text)

    def write(self, content: Dict, filename: str) -> None:
        yaml.dump(content, open(filename, "w"), sort_keys=self.options.sort_keys)

    def format(self, content: str) -> str:
        return content
