from dataclasses import dataclass, field


@dataclass
class GetData:
    type: str = "None"
    data: str = "None"

