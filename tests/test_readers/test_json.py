import pytest
from sops_git_hooks.readers.json import JsonConverter
from tests.fixtures import (
    plaintext_file_json,
    encrypted_file_json,
    content_json,
    temp_filename,
)

converter = JsonConverter()


@pytest.mark.parametrize(
    "filename,expected",
    [(plaintext_file_json, content_json), (encrypted_file_json, content_json)],
)
def test_read_json(filename, expected):
    file_content = converter.read(filename=filename)
    assert file_content == expected


def test_write_json():
    content = content_json
    temp_filename_json = temp_filename + ".json"
    converter.write(content, filename=temp_filename_json)
    assert open(temp_filename_json, "r").read() == open(plaintext_file_json, "r").read()
