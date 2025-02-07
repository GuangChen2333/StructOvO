from typing import TypeVar, Optional
from ._types import BaseType, FixedString
from ._enums import Endianness

T = TypeVar('T', bound='Pack')


class Pack:
    @classmethod
    def build(cls, endianness: Optional[Endianness] = Endianness.NATIVE) -> bytes:
        anns = cls.__annotations__
        data = cls.__dict__

        result_list = []

        for key, type_class in anns.items():
            if not issubclass(type_class, BaseType) and not type_class is bytes:
                raise ValueError(f"{type_class} is not an instance of bytes or structovo.BaseType")

            if type_class is bytes:
                result_list.append(data.get(key))
                continue

            elif type_class is FixedString:
                try:
                    value: FixedString = FixedString(data[key][0], data[key][1])
                except IndexError:
                    raise ValueError('Using x: FixedString = (value: bytes, length: int)')

            else:
                value: BaseType = type_class(data.get(key))

            result_list.append(value.encode(endianness))

        return b''.join(result_list)
