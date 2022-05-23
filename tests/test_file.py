import os
from pathlib import Path
from shutil import ReadError
import pytest
from sops_git_hooks.config import Config
from sops_git_hooks.file import FileHandler, PlaintextFile
from sops_git_hooks.readers.json import JsonConverter
from sops_git_hooks.readers.main_reader import MainReader
from tests.fixtures import (
    plaintext_file_json,
    content_json,
    encrypted_file_json,
    plaintext_file_no_enc_json,
    plaintext_file_wrong_enc_json,
)


@pytest.fixture
def reader() -> MainReader:
    reader = MainReader()
    json_reader = JsonConverter()
    reader.register_reader(json_reader, extensions=["json"])
    return reader


@pytest.fixture
def config() -> Config:
    return Config()


@pytest.fixture
def filehandler(reader, config) -> FileHandler:
    return FileHandler(reader=reader, config=config)


@pytest.fixture
def plaintext_file(filehandler: FileHandler) -> PlaintextFile:
    return filehandler.create_plaintext(plaintext_file_json)


@pytest.fixture
def plaintext_file_no_enc(filehandler: FileHandler) -> PlaintextFile:
    return filehandler.create_plaintext(plaintext_file_no_enc_json)


@pytest.fixture
def plaintext_file_wrong_enc(filehandler: FileHandler) -> PlaintextFile:
    return filehandler.create_plaintext(plaintext_file_wrong_enc_json)


def test_filehander_create_plaintext(filehandler: FileHandler):
    pt_file = filehandler.create_plaintext(plaintext_file_json)
    assert pt_file.filename == plaintext_file_json
    assert pt_file.content == content_json


def test_plaintext_file_create_encrypted(plaintext_file: PlaintextFile):
    encrypted = plaintext_file.create_encrypted()
    assert encrypted.filename == encrypted_file_json
    assert encrypted.content == content_json


def test_plaintext_file_create_encrypted_no_file(plaintext_file_no_enc: PlaintextFile):
    encrypted = plaintext_file_no_enc.create_encrypted()
    assert encrypted.content is None


def test_plaintextfile_equality(plaintext_file: PlaintextFile):
    assert plaintext_file.check_equality()


def test_plaintextfile_equality_no_enc(plaintext_file_no_enc: PlaintextFile):
    assert not plaintext_file_no_enc.check_equality()


def test_plaintextfile_equality_wrong_enc(plaintext_file_wrong_enc: PlaintextFile):
    assert not plaintext_file_wrong_enc.check_equality()


def test_plaintextfile_encrypt_no_enc(plaintext_file_no_enc: PlaintextFile):
    plaintext_file_no_enc.encrypt()
    assert Path(plaintext_file_no_enc.encrypted_filename).is_file()
    os.remove(plaintext_file_no_enc.encrypted_filename)
