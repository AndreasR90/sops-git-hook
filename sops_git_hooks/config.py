from dataclasses import dataclass


@dataclass
class Config:
    encrypt_string: str = "encrypted"


config = Config()
