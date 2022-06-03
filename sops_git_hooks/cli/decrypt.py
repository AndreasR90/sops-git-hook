from sops_git_hooks.cli.arguments import extract_config, setup_main_reader
from sops_git_hooks.config import AppConfig
from sops_git_hooks.file import PlaintextFile

from sops_git_hooks.readers.main_reader import MainReader

config_file = ".secrets.yaml"


def decrypt_secret(secret: str, main_reader: MainReader, app_config: AppConfig) -> bool:
    plain_text = PlaintextFile(secret, reader=main_reader, config=app_config)
    are_equal = plain_text.check_equality()
    if not are_equal:
        plain_text.decrypt(overwrite=True)
        return True
    return False


def main_decrypt():  # config_file: str):
    configuration, app_config = extract_config(config_file=config_file)
    configuration, app_config = extract_config(config_file=config_file)
    main_reader = setup_main_reader(app_config=app_config)
    created_plain_text = []
    for secret in configuration.secrets:
        modified = decrypt_secret(
            secret=secret, main_reader=main_reader, app_config=app_config
        )
        if modified:
            created_plain_text.append(secret)
    if len(created_plain_text):
        print(
            "The following files were created/modified\n\t"
            + "\n\t".join(created_plain_text)
        )


if __name__ == "__main__":
    main_decrypt()  # config_file=config_file)
    # main_encrypt(config_file=config_file)
