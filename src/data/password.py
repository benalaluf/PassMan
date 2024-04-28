import datetime
from dataclasses import dataclass


@dataclass
class Password:
    name: str
    password: str
    date: datetime.datetime
    note: str