from dataclasses import dataclass


@dataclass
class AuthData:
    type: str = "None"
    username: str = "None"
    password: str = "None"
    mail: str = "None"
    two_fa_code: str = "None"
