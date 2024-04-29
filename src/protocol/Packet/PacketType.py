from enum import Enum


class PacketType(Enum):
    REGISTER = 1
    LOGIN = 2
    ADDITEM = 3
    DELETEITEM = 9
    GETUSERDOC= 4
    DATA=10
    REQ = 5
    SESSION = 6
    SUCCESS = 69
    FAIL = 42
