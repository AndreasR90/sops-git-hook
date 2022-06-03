import pytest
from sops_git_hooks.sops import Sops, SopsException


def test_check_location():
    with pytest.raises(SopsException):
        Sops(location="my_non_existing_project")
