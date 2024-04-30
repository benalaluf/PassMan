from enum import Enum


class PacketType(Enum):
    REGISTER = 1
    LOGIN = 2
    POST = 3
    GET = 4
    SUCCESS = 69
    FAIL = 42
