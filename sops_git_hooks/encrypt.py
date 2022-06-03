import sys
from sops_git_hooks.base_file_operations import FileChecker
from sops_git_hooks.config import Config, AppConfig
from sops_git_hooks.file import PlaintextFile
from sops_git_hooks.readers.json import JsonConverter
from sops_git_hooks.readers.yaml import YamlConverter
from sops_git_hooks.readers.ini import IniConverter
from sops_git_hooks.readers.main_reader import MainReader
from sops_git_hooks.sops import Sops

config_file = ".secrets.yaml"


def setup_main_reader(app_config: AppConfig) -> MainReader:
    file_checker = FileChecker(sops=Sops(app_config.sops_location))
    main_reader = MainReader(file_checker=file_checker)
    main_reader.register_reader(converter=JsonConverter(), extensions=["json"])
    main_reader.register_reader(converter=YamlConverter(), extensions=["yaml", "yml"])
    main_reader.register_reader(converter=IniConverter(), extensions=["ini"])
    return main_reader


def encrypt_secret(secret: str, main_reader: MainReader, app_config: AppConfig) -> bool:
    plain_text = PlaintextFile(filename=secret, reader=main_reader, config=app_config)
    is_encrypted = plain_text.check_equality()
    if not is_encrypted:
        plain_text.encrypt(overwrite=True)
        return True
    return False


def main(config_file: str):
    configuration = Config.from_yaml(config_file)
    app_config = configuration.app_config
    main_reader = setup_main_reader(app_config=app_config)
    modified_secrets = []
    for secret in configuration.secrets:
        modified = encrypt_secret(
            secret, main_reader=main_reader, app_config=app_config
        )
        if modified:
            modified_secrets.append(secret)
    if len(modified_secrets) != 0:
        print(
            "The following secrets are not correctly encrypted"
            + " , ".join(modified_secrets)
        )
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main(config_file=config_file)
