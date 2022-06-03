from setuptools import find_packages, setup

setup(
    name="sops_git_hooks",
    # package_dir={"": "src"},
    packages=find_packages("."),
    entry_points={
        "console_scripts": [
            "encrypt=sops_git_hooks.cli.encrypt:main_encrypt",
            "decrypt=sops_git_hooks.cli.decrypt:main_decrypt",
        ]
    },
    install_requires=["pyyaml"],
)
