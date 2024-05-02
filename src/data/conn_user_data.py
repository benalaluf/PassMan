from dataclasses import dataclass


@dataclass
class ConnUserData:
    username: str = None
    password: str = None
    key_salt: str = None
    key: str = None
    session: str = None
