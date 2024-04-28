from enum import Enum


class PacketType(Enum):
    REGISTER = 1
    LOGIN = 2
    ADDPASS = 3
    READPASS = 4
    REQ = 5
    SESSION = 6
    SUCCESS = 69
    FAIL = 42
