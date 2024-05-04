from dataclasses import dataclass


@dataclass
class PostData:
    session: str = "None"
    type: str = "None"
    item_type: str = "None"
    data: dict = None


