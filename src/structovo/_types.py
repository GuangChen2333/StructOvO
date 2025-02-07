from typing import Any, Tuple, Optional, Type
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

    def raise_if_invalid(self):
        result, real = self.check_validation()
        if not result:
            raise ValueError(f"Invalid value type, it must be a {real}")

    @property
    def value(self):
        return self._value

    @abstractmethod
    def encode(self, endianness: Endianness) -> bytes:
        pass

    @abstractmethod
    def check_validation(self) -> Tuple[bool, Type]:
        pass


class PADDING(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = self.value is None or isinstance(self.value, int)
        return result, Optional[int]

    def encode(self, endianness: Endianness) -> bytes:
        return b'\x00' * (self.value if self.value else 1)


class BYTE(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, bytes)
        return result, bytes

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('c', endianness)


class CHAR(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('b', endianness)


class UCHAR(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('B', endianness)


class BOOL(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, bool)
        return result, bool

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('?', endianness)


class SHORT(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('h', endianness)


class USHORT(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('H', endianness)


class INT(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('i', endianness)


class UINT(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('I', endianness)


class LONG(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('l', endianness)


class ULONG(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('L', endianness)


class LONGLONG(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('q', endianness)


class ULONGLONG(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('Q', endianness)


class SSIZET(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('n', endianness)


class SIZET(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('N', endianness)


class FLOAT(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, float)
        return result, float

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('f', endianness)


class DOUBLE(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, float)
        return result, float

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('d', endianness)


class FixedString(BaseType):
    def check_validation(self):
        return (
                not isinstance(self.value, tuple)
                or not isinstance(self.value[0], bytes)
                or not isinstance(self.value[1], int)
        ), Tuple[bytes, int]

    def __new__(cls, value: Tuple[bytes, int]):
        instance = super().__new__(cls, value)

        instance._value = value[0]
        instance._length = value[1]

        return instance

    @property
    def length(self):
        return self._length

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack(f'{self.length}s', endianness)


class LengthPrefixedString(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, bytes)
        return result, bytes

    def encode(self, endianness: Endianness) -> bytes:
        length = len(self.value)
        if length > 255:
            raise ValueError("String length exceeds maximum allowed length (255 bytes)")
        return pack(f'{endianness.value}B', length) + self.value


class BINARY16(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, float)
        return result, float

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('e', endianness)


class UnsignedPointer(BaseType):
    def check_validation(self) -> Tuple[bool, Type]:
        result = isinstance(self.value, int)
        return result, int

    def encode(self, endianness: Endianness) -> bytes:
        return self._pack('P', endianness)
