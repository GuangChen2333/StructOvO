from enum import StrEnum


class Endianness(StrEnum):
    BIG = '>'
    LITTLE = '<'
    NETWORK = '!'
    NATIVE = '@'
