from dataclasses import dataclass, field


@dataclass
class GetData:
    type: str = "None"
    data: dict = field(default_factory=dict)

