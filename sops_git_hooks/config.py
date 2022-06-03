from dataclasses import dataclass, field, fields
from typing import Dict, List

import yaml


@dataclass
class AppConfig:
    encrypt_string: str = "encrypted"
    sops_location: str = "sops"
    readers: Dict = field(default_factory=dict)


@dataclass
class Config:
    app_config: AppConfig = field(default_factory=AppConfig)
    secrets: List[str] = field(default_factory=list)

    @staticmethod
    def from_yaml(filename: str):
        configuration: Dict = yaml.safe_load(open(filename, "r"))
        kwargs = {}
        for fld in fields(AppConfig):
            fld_name = fld.name
            if fld_name in configuration:
                kwargs[fld_name] = configuration[fld_name]
        app_config = AppConfig(**kwargs)
        return Config(secrets=configuration.get("secrets", []), app_config=app_config)
