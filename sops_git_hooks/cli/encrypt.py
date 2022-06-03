import sys
from sops_git_hooks.cli.arguments import extract_config, setup_main_reader
from sops_git_hooks.config import AppConfig
from sops_git_hooks.file import PlaintextFile

from sops_git_hooks.readers.main_reader import MainReader

config_file = ".secrets.yaml"


def encrypt_secret(secret: str, main_reader: MainReader, app_config: AppConfig) -> bool:
    plain_text = PlaintextFile(filename=secret, reader=main_reader, config=app_config)
    is_encrypted = plain_text.check_equality()
    if not is_encrypted:
        plain_text.encrypt(overwrite=True)
        return True
    return False


def main_encrypt():  # config_file: str):
    configuration, app_config = extract_config(config_file=config_file)
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
            "The following secrets were not correctly encrypted"
            + "but have been fixed:\n\t"
            + "\n\t".join(modified_secrets)
        )
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main_encrypt()  # config_file=config_file)
