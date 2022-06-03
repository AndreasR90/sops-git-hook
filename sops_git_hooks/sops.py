import subprocess
from typing import List
from shutil import which


class SopsException(Exception):
    pass


SOPS_REGEX = r"ENC.AES256"


class Sops:
    def __init__(self, location: str = "sops"):
        self.location = location
        self._check_input()

    def _check_input(self):
        self._check_location()

    def _check_location(self):
        sops_exists = which(self.location) is not None
        if not sops_exists:
            raise SopsException("Sops not found. Make sure it is installed")

    def encrypt(self, filename: str) -> str:
        args = ["--encrypt", filename]
        return self._call(args)

    def _call(self, args: List[str]) -> str:
        args = [self.location] + args
        plain_text_byte = self._sys_call(args)
        plain_text = plain_text_byte.decode()
        return plain_text

    def _sys_call(self, args):
        plain_text_byte = subprocess.check_output(args)
        return plain_text_byte

    def decrypt(self, filename: str) -> str:
        args = ["--decrypt", filename]
        return self._call(args)
