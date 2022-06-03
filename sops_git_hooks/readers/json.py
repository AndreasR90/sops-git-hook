from dataclasses import dataclass
import json
from typing import Dict, Union
from sops_git_hooks.base_file_operations import FileChecker
from sops_git_hooks.readers.base import Converter


@dataclass
class JsonOptions:
    indent: Union[str, int] = 4


class JsonConverter(Converter):
    def __init__(
        self,
        options: JsonOptions = JsonOptions(),
        file_checker: FileChecker = FileChecker(),
    ):
        self.options: JsonOptions = options
        super().__init__(file_checker=file_checker)

    def write(self, content: Dict, filename: str):
        json.dump(content, open(filename, "w"), indent=self.options.indent)

    def read(self, filename):
        plain_text = self.file_checker.load_file(filename=filename)
        return json.loads(plain_text)
