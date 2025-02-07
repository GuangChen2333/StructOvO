# StructOvO

A Python library offering a more concise syntax alternative to the standard struct module.

## Usage

```python
from structovo import *


class PackA(Pack):
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


r = PackA.build(endianness=Endianness.NATIVE)
print(r)
```

And you will get:

```text
b'\x00A\xff\x01\x00\xfe\xff\x02\x00\xfd\xff\xff\xff\x03\x00\x00\x00\xfc\xff\xff\xff\x04\x00\x00\x00\xfb\xff\xff\xff\xff\xff\xff\xff\x05\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00"\x00\x00\x00\x00\x00\x00\x00HB\xc3\xf5H@\x1f\x85\xebQ\xb8\x1e\t@hello\x00\x00\x00\x00\x00\x05world!\x07\x00\r\x00\x00\x00\x00'
```