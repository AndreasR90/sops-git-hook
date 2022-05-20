from importlib.metadata import entry_points
from setuptools import find_packages, setup

setup(
    name="sops_git_hooks",
    # package_dir={"": "src"},
    packages=find_packages("."),
    entry_points={"console_scripts": ["encrypt=sops_git_hooks.encrypt:main"]},
)

