import pytest
from sops_git_hooks.readers.main_reader import MainReader, ReaderError
from sops_git_hooks.readers.json import JsonConverter
from tests.fixtures import plaintext_file_json, content_json, temp_filename
from tests.test_base_file_operations import assert_files_equal

temp_filename_json = temp_filename + ".json"


def test_main_reader_read():
    reader = MainReader()
    reader.register_reader(JsonConverter(), extensions=["json"])
    content = reader.read(plaintext_file_json)
    assert content == content_json


def test_main_reader_getitem_exception():
    reader = MainReader()
    with pytest.raises(ReaderError):
        reader["json"]


def test_main_reader_write():
    reader = MainReader()
    reader.register_reader(JsonConverter(), extensions=["json"])
    reader.write(content_json, filename=temp_filename_json)
    assert_files_equal(
        temp_filename_json, plaintext_file_json, delete_files=[temp_filename_json]
    )
