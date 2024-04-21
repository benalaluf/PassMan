from enum import Enum


class PacketType(Enum):
    REGISTER = 1
    LOGIN = 2
    ADDPASS = 3
    READPASS = 4
    SUCCESS = 69
    FAIL = 42
