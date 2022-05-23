from sops_git_hooks.base_file_operations import encrypted_version
from .readers.main_reader import MainReader
from .config import Config
from pathlib import Path

from .sops import sops


class EncryptedFile:
    def __init__(self, filename: str, reader: MainReader, config: Config):
        self.filename = filename
        self.reader = reader
        self.config = config
        if Path(self.filename).is_file():
            self.content = self.reader.read(self.filename)
        else:
            self.content = None


class PlaintextFile:
    def __init__(self, filename: str, reader: MainReader, config: Config):
        self.filename = filename
        self.reader = reader
        self.config = config
        self.content = reader.read(filename=self.filename)
        self.encrypted_filename = encrypted_version(
            filename=self.filename, encrypt_string=config.encrypt_string
        )
        self.encrypted_file = self.create_encrypted()

    def create_encrypted(self):
        return EncryptedFile(
            filename=self.encrypted_filename, reader=self.reader, config=self.config
        )

    def check_equality(self):
        return self.content == self.encrypted_file.content

    def encrypt(self, overwrite=True):
        encryption = sops.encrypt(filename=self.filename)
        if overwrite:
            with open(self.encrypted_filename, "w") as file:
                file.write(encryption)

    def ensure_latest_encryption(self) -> bool:
        is_latest = self.check_equality()
        if is_latest:
            changed = False
        else:
            self.encrypt(overwrite=True)
            changed = True
        return changed


class FileHandler:
    def __init__(self, reader: MainReader, config: Config):
        self.reader = reader
        self.config = config

    def create_plaintext(self, filename: str) -> PlaintextFile:
        return PlaintextFile(filename=filename, reader=self.reader, config=self.config)

