import datetime
import uuid
from dataclasses import dataclass, asdict


@dataclass
class CardData:
    bank_name: str
    card_number: str
    cvv: str
    expr_date: str
    id:str = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())


    def validate_date(self):
        pass


if __name__ == '__main__':
    s = CardData("name", "458011233332123d", "879", str(datetime.datetime.now()))
    s2 = CardData("url", "ben", "1234", str(datetime.datetime.now()))
    print(s)
    print(s2)
