from pathlib import Path

plaintext_file_json = str(Path(__file__).parent / "data/sample.json")
encrypted_file_json = str(Path(__file__).parent / "data/sample.encrypted.json")
plaintext_file_no_enc_json = str(Path(__file__).parent / "data/sample_no_enc.json")
plaintext_file_wrong_enc_json = str(
    Path(__file__).parent / "data/sample_wrong_enc.json"
)
encrypted_file_wrong_enc_json = str(
    Path(__file__).parent / "data/sample_wrong_enc.encrypted.json"
)

temp_filename = "test"

content_json = {
    "firstName": "John",
    "lastName": "Smith",
    "age": 25.4,
    "address": {
        "city": "New York",
        "postalCode": "10021-3100",
        "state": "NY",
        "streetAddress": "21 2nd Street",
    },
    "phoneNumbers": [
        {"number": "212 555-1234", "type": "home"},
        {"number": "646 555-4567", "type": "office"},
    ],
    "anEmptyValue": "",
}

plaintext_file_ini = str(Path(__file__).parent / "data/sample.ini")
encrypted_file_ini = str(Path(__file__).parent / "data/sample.encrypted.ini")
content_ini = {
    "name": {"firstName": "John", "lastName": "Smith", "age": "25.4",},
    "address": {
        "city": "New York",
        "postalCode": "10021-3100",
        "state": "NY",
        "streetAddress": "21 2nd Street",
    },
    "phoneNumbers": {"home": "212 555-1234", "office": "646 555-4567",},
    "not private": {"notsecret_unencrypted": "hi there!"},
}

plaintext_file_yaml = str(Path(__file__).parent / "data/sample.yaml")

content_yaml = {
    "firstName": "John",
    "lastName": "Smith",
    "age": 25.4,
    "address": {
        "city": "New York",
        "postalCode": "10021-3100",
        "state": "NY",
        "streetAddress": "21 2nd Street",
    },
    "phoneNumbers": [
        {"number": "212 555-1234", "type": "home"},
        {"number": "646 555-4567", "type": "office"},
    ],
}
