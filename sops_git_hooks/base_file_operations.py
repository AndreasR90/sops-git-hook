import re

from .sops import SOPS_REGEX, Sops


class FileChecker:
    def __init__(self, sops: Sops = Sops()):
        self.sops: Sops = sops

    def get_file_extension(self, filename: str):
        splitted = filename.split(".")
        needed_fields = 1
        if splitted[0] == "":
            needed_fields += 1
        if len(splitted) <= needed_fields:
            return ""
        return splitted[-1]

    def is_file_encrypted(self, filename: str):
        with open(filename, "r") as file:
            lines = file.read()
            is_encrypted = bool(
                re.search(SOPS_REGEX, lines, flags=re.IGNORECASE | re.MULTILINE)
            )
        return is_encrypted

    def load_file(self, filename: str) -> str:
        encrypted = self.is_file_encrypted(filename=filename)
        if encrypted:
            return self.load_decrypted_file(filename=filename)
        return self.load_plaintext_file(filename=filename)

    def load_plaintext_file(self, filename: str) -> str:
        with open(filename, "r") as file:
            return file.read()

    def load_decrypted_file(self, filename: str) -> str:
        return self.sops.decrypt(
            filename
        )  # subprocess.check_output(["sops", "-d", filename])

    def encrypted_version(
        self, filename: str, encrypt_string: str = "encrypted"
    ) -> str:
        extension = self.get_file_extension(filename=filename)
        basename = filename.replace(f".{extension}", "")
        return ".".join([basename, encrypt_string, extension])
