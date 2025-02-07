from typing import Any
from abc import ABC, abstractmethod
from struct import pack

from ._enums import Endianness


class BaseType(ABC):
    def __new__(cls, value: Any):
        instance = super().__new__(cls)
        instance._value = value
        return instance

    def _pack(self, fmt: str, endianness: Endianness) -> bytes:
        return pack(f'{endianness.value}{fmt}', self.value)

    @property
    def value(self):
        return self._value

    @abstractmethod
    def encode(self, endianness: Endianness) -> bytes:
        pass


class PADDING(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return b'\x00' * (self.value if self.value else 1)


class BYTE(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('c', endianness)


class CHAR(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('b', endianness)


class UCHAR(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('B', endianness)


class BOOL(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('?', endianness)


class SHORT(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('h', endianness)


class USHORT(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('H', endianness)


class INT(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('i', endianness)


class UINT(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('I', endianness)


class LONG(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('l', endianness)


class ULONG(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('L', endianness)


class LONGLONG(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('q', endianness)


class ULONGLONG(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('Q', endianness)


class SSIZET(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('n', endianness)


class SIZET(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('N', endianness)


class FLOAT(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('f', endianness)


class DOUBLE(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('d', endianness)


class FixedString(BaseType):
    def __new__(cls, value: bytes, length: int):
        instance = super().__new__(cls, value)
        instance._value = value
        instance._length = length
        return instance

    @property
    def length(self):
        return self._length

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack(f'{self.length}s', endianness)


class LengthPrefixedString(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        length = len(self.value)
        if length > 255:
            raise ValueError("String length exceeds maximum allowed length (255 bytes)")
        return pack(f'{endianness.value}B', length) + self.value


class BINARY16(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('e', endianness)


class UnsignedPointer(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('P', endianness)
