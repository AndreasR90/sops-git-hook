from typing import Tuple
from sops_git_hooks.base_file_operations import FileChecker
from sops_git_hooks.config import AppConfig, Config

from sops_git_hooks.readers.main_reader import MainReader
from sops_git_hooks.readers.to_register import converters
from sops_git_hooks.sops import Sops


def extract_config(config_file) -> Tuple[Config, AppConfig]:
    configuration = Config.from_yaml(config_file)
    app_config = configuration.app_config
    return configuration, app_config


def setup_main_reader(app_config: AppConfig) -> MainReader:
    file_checker = FileChecker(sops=Sops(app_config.sops_location))
    main_reader = MainReader(file_checker=file_checker)
    for converter in converters:
        option_args = {}
        for extension, values in app_config.readers.items():
            if extension in converter.extensions:
                option_args = values
                break

        main_reader.register_reader(
            converter.converter(options=converter.converter_options(**option_args)),
            extensions=converter.extensions,
        )

    return main_reader
