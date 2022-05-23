from argparse import ArgumentError
import subprocess
from typing import Optional


class Sops:
    def __init__(self, location: str = "sops"):
        self.location = location

    def encrypt(self, filename: str) -> str:

        args = [self.location, "--encrypt", filename]
        plain_text_byte = subprocess.check_output(args)
        plain_text = plain_text_byte.decode()
        return plain_text


sops = Sops()
