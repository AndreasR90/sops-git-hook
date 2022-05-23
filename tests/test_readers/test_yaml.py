from sops_git_hooks.readers.yaml import YamlConverter
from tests.fixtures import plaintext_file_yaml, content_yaml, temp_filename
import pytest

converter = YamlConverter()


@pytest.mark.parametrize(
    "filename,expected", [(plaintext_file_yaml, content_yaml),],
)
def test_read_yaml(filename, expected):
    file_content = converter.read(filename=filename)
    assert file_content == expected


def test_write_yaml():
    content = content_yaml
    temp_filename_yaml = temp_filename + ".yaml"
    converter.write(content, filename=temp_filename_yaml)
    assert open(temp_filename_yaml, "r").read() == open(plaintext_file_yaml, "r").read()
