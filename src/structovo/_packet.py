from typing import TypeVar, Optional
from ._types import BaseType
from ._enums import Endianness

T = TypeVar('T', bound='Pack')


class Packet:
    @classmethod
    def build(cls, endianness: Optional[Endianness] = Endianness.NATIVE) -> bytes:
        anns = cls.__annotations__
        data = cls.__dict__

        result_list = []

        for key, type_class in anns.items():
            try:
                if not issubclass(type_class, BaseType) and not type_class is bytes:
                    raise ValueError(f"{type_class} is not an instance of bytes or structovo.BaseType")

                if type_class is bytes:
                    result_list.append(data.get(key))
                    continue

                else:
                    value: BaseType = type_class(data.get(key))

                value.raise_if_invalid()
                result_list.append(value.encode(endianness))
            except Exception as e:
                raise ValueError(f"Key {key} raised that {e}, and now it is a {type(data.get(key))}.")


        return b''.join(result_list)
