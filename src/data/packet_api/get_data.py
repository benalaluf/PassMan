from dataclasses import dataclass


@dataclass
class GetData:
    session: str = "None"
    type: str = "None"

