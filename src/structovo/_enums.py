from enum import Enum

class Endianness(Enum):
    BIG = '>'
    LITTLE = '<'
    NETWORK = '!'
    NATIVE = '@'
