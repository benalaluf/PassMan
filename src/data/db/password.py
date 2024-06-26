import datetime
import uuid
from dataclasses import dataclass, asdict


@dataclass
class PasswordData:
    url: str
    username: str
    password: str
    date: str
    id:str = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())


if __name__ == '__main__':
    s = PasswordData("url", "ben", "1234", str(datetime.datetime.now()))
    s2 = PasswordData("url", "ben", "1234", str(datetime.datetime.now()))
    print(s)
    print(s2)
