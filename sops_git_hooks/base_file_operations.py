import configparser
from dataclasses import dataclass
import subprocess
import json
import re
import yaml
from typing import Callable, Dict, Optional, Union

SOPS_REGEX = r"ENC.AES256"


class Sops:
    def __init__(self):
        self.sops_location = "sops"

    def encrypt(self, filename, inplace: bool = False) -> str:
        additional_arguments = []
        if inplace:
            additional_arguments.append("--inplace")
        return subprocess.check_output(
            [self.sops_location, filename] + additional_arguments
        )


def get_file_extension(filename: str):
    splitted = filename.split(".")
    needed_fields = 1
    if splitted[0] == "":
        needed_fields += 1
    if len(splitted) <= needed_fields:
        return ""
    return splitted[-1]


def is_file_encrypted(filename: str):
    with open(filename, "r") as file:
        lines = file.read()
        is_encrypted = bool(
            re.search(SOPS_REGEX, lines, flags=re.IGNORECASE | re.MULTILINE)
        )
    return is_encrypted


def load_file(filename: str) -> str:
    encrypted = is_file_encrypted(filename=filename)
    if encrypted:
        return load_decrypted_file(filename=filename)
    return load_plaintext_file(filename=filename)


def load_plaintext_file(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read()


def load_decrypted_file(filename: str) -> str:
    plain_text_byte = subprocess.check_output(["sops", "-d", filename])
    plain_text = plain_text_byte.decode()
    return plain_text


def encrypted_version(filename: str, encrypt_string: str = "encrypted") -> str:
    extension = get_file_extension(filename=filename)
    basename = filename.replace(f".{extension}", "")
    return ".".join([basename, encrypt_string, extension])

