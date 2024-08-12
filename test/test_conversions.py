import ctypes.util
import ctypes.wintypes
from test_base import TestBase

from simdstring import (
    SIMDString,
    to_string,
)

import ctypes
import sys


class ConversionTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Conversion Tests "

    def start(self) -> None:
        simdstring1 = SIMDString(to_string(1234567890))
        string1 = str(1234567890)

        self.compare_add("int", simdstring1, len(string1), string1)

        simdstring1 = to_string(ctypes.c_uint32(123456789).value)
        string1 = str(ctypes.c_uint32(123456789).value)
        self.compare_add("unsigned int", simdstring1, len(string1), string1)

        simdstring1 = to_string(ctypes.c_long(123456789).value)
        string1 = str(ctypes.c_long(123456789).value)
        self.compare_add("long", simdstring1, len(string1), string1)

        simdstring1 = to_string(ctypes.c_ulong(123456789).value)
        string1 = str(ctypes.c_ulong(123456789).value)
        self.compare_add("unsigned long", simdstring1, len(string1), string1)

        simdstring1 = to_string(ctypes.c_longlong(123456789).value)
        string1 = str(ctypes.c_longlong(123456789).value)
        self.compare_add("long long", simdstring1, len(string1), string1)

        simdstring1 = to_string(ctypes.c_ulonglong(123456789).value)
        string1 = str(ctypes.c_ulonglong(123456789).value)
        self.compare_add("unsigned long long", simdstring1, len(string1), string1)

        simdstring1 = to_string(sys.maxsize)
        string1 = str(sys.maxsize)
        self.compare_add("int max", simdstring1, len(string1), string1)

        simdstring1 = to_string(-sys.maxsize - 1)
        string1 = str(-sys.maxsize - 1)
        self.compare_add("int min", simdstring1, len(string1), string1)

        simdstring1 = to_string(
            123456789012345678901234567890.12345678901234567890123456789012345678901234567890123456789012345678901234567890
        )
        string1 = str(
            123456789012345678901234567890.12345678901234567890123456789012345678901234567890123456789012345678901234567890
        )
        self.compare_add("float", simdstring1, len(string1), string1)
