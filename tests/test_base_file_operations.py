import json
import os
import pytest
from sops_git_hooks.base_file_operations import FileChecker
from tests.fixtures import (
    plaintext_file_ini,
    plaintext_file_json,
    plaintext_file_yaml,
    content_json,
    encrypted_file_ini,
    encrypted_file_json,
)

file_checker = FileChecker()


@pytest.mark.parametrize(
    "filename,expected",
    [("a.json", "json"), ("a.b.json", "json"), ("a", ""), (".a", "")],
)
def test_extension(filename, expected):
    extension = file_checker.get_file_extension(filename)
    assert extension == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        (plaintext_file_json, False),
        (encrypted_file_json, True),
        (plaintext_file_ini, False),
        (encrypted_file_ini, True),
        (plaintext_file_yaml, False),
    ],
)
def test_is_file_encrypted(filename, expected):
    is_encrypted = file_checker.is_file_encrypted(filename)
    assert is_encrypted == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        # (plaintext_file_ini, content_ini),
        (plaintext_file_json, content_json),
        (encrypted_file_json, content_json),
    ],
)
def test_load_file(filename, expected):
    file_content = file_checker.load_file(filename)
    assert json.loads(file_content) == expected


def test_load_decrypted_file():
    filename = encrypted_file_json
    plain_text = file_checker.load_decrypted_file(filename=filename)
    assert json.loads(plain_text) == content_json


def test_load_plaintext_file():
    filename = plaintext_file_json
    plain_text = file_checker.load_plaintext_file(filename=filename)
    assert json.loads(plain_text) == content_json


def assert_files_equal(file1, file2, delete_files=None):
    return_value = open(file1, "r").read() == open(file2, "r").read()
    delete_files = delete_files or []
    for file in delete_files:
        os.remove(file)
    assert return_value


@pytest.mark.parametrize(
    "filename,encrypt_string,encrypted_version_expected",
    [
        ("a.json", "enc", "a.enc.json"),
        ("a.ini", "encrypted", "a.encrypted.ini"),
        ("a.json", None, "a.encrypted.json"),
    ],
)
def test_encrypted_version(filename, encrypt_string, encrypted_version_expected):
    if encrypt_string is not None:
        encrypted_version_calculated = file_checker.encrypted_version(
            filename, encrypt_string=encrypt_string
        )
    else:
        encrypted_version_calculated = file_checker.encrypted_version(filename)
    assert encrypted_version_calculated == encrypted_version_expected


# def test_encrypt_secret():
#     filename = plaintext_file_json
#     encrypted = encrypt_secret(filename)
#     assert_files_equal(encrypted, encrypted_file_json)
