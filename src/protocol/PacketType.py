from enum import Enum


class PacketType(Enum):
    AUTH = 1
    POST = 3
    GET = 4
    SUCCESS = 69
    FAIL = 42
