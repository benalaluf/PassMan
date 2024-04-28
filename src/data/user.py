import datetime
from dataclasses import dataclass


@dataclass
class UserData:
    username: str
    password: str
    mail: str
    pass_salt: str
    key_salt: str
