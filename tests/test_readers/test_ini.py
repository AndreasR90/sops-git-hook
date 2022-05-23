from sops_git_hooks.readers.ini import IniConverter
from tests.fixtures import (
    plaintext_file_ini,
    content_ini,
    encrypted_file_ini,
    temp_filename,
)
import pytest

converter = IniConverter()


@pytest.mark.parametrize(
    "filename,expected",
    [(plaintext_file_ini, content_ini), (encrypted_file_ini, content_ini)],
)
def test_read_ini(filename, expected):
    file_content = converter.read(filename=filename)
    assert file_content == expected


def test_write_ini():
    content = content_ini
    temp_filename_ini = temp_filename + ".ini"
    converter.write(content, filename=temp_filename_ini)
    assert open(temp_filename_ini, "r").read() == open(plaintext_file_ini, "r").read()
