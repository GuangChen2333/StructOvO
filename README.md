# StructOvO

![GitHub License](https://img.shields.io/github/license/GuangChen2333/StructOvO?style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/GuangChen2333/StructOvO?style=flat-square)
![PyPi](https://img.shields.io/pypi/v/structovo?style=flat-square)
![Downloads](https://img.shields.io/pypi/dm/structovo?style=flat-square)
![Python](https://img.shields.io/pypi/pyversions/structovo?style=flat-square)

A Python library offering a more concise syntax for data packing.

## Installation

- From `pypi`

```shell
pip install structovo
```

## Usage

```python
from structovo import *


class PackA(Packet):
    a: PADDING
    b: BYTE = b'A'
    c: CHAR = -1
    d: UCHAR = 1
    e: BOOL = False
    f: SHORT = -2
    g: USHORT = 2
    h: INT = -3
    i: UINT = 3
    j: LONG = -4
    k: ULONG = 4
    l: LONGLONG = -5
    m: ULONGLONG = 5
    n: SIZET = 12
    o: SSIZET = 34
    p: BINARY16 = 3.14
    q: FLOAT = 3.14
    r: DOUBLE = 3.14
    s: FixedString = (b"hello", 10)
    t: LengthPrefixedString = b"world"
    u: UnsignedPointer = 0x0d000721
    v: bytes = b'raw_bytes'


r = PackA.build(endianness=Endianness.NATIVE)
hex_list = [format(byte, '02x') for byte in r]
hex_str = ' '.join(hex_list)
print(hex_str)
```

And you will get:

```text
00 41 ff 01 00 fe ff 02 00 fd ff ff ff 03 00 00 00 fc ff ff ff 04 00 00 00 fb ff ff ff ff ff ff ff 05 00 00 00 00 00 00 00 0c 00 00 00 00 00 00 00 22 00 00 00 00 00 00 00 48 42 c3 f5 48 40 1f 85 eb 51 b8 1e 09 40 68 65 6c 6c 6f 00 00 00 00 00 05 77 6f 72 6c 64 21 07 00 0d 00 00 00 00 72 61 77 5f 62 79 74 65 73
```

## Advance

### Supported Endianness

- `Endianness.BIG`: Big-endian
- `Endianness.LITTLE`: Little-endian
- `Endianness.NETWORK`: Big-endian
- `Endianness.NATIVE`: Depend on your device (Default)

### Custom Data Types

You can define your own data types by simply inheriting the `BaseType` class:

```python
from structovo import BaseType, Endianness


class MyDataType(BaseType):
    def encode(self, endianness: Endianness) -> bytes:
        return ...
```