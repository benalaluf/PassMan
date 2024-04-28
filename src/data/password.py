import datetime
from dataclasses import dataclass, asdict


@dataclass
class PasswordData:
    url: str
    username: str
    password: str
    date: str


if __name__ == '__main__':
    s = PasswordData("url", "ben", "1234", str(datetime.datetime.now()))

    d = asdict(s)
    print(d)
    for key,value in d.items():
        d[key] = value+"a"

    print(d)
