from test_base import TestBase
from utility import sample_string

from simdstring import SIMDString


class CtorTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Constructor Tests "

    def start(self) -> None:
        simdstring0 = SIMDString()
        simdstring1 = SIMDString("a")
        simdstring2 = SIMDString("0123456789abcdefghijklmnopqrstuvwxyz")
        simdstring3 = SIMDString(simdstring2, 10)
        simdstring4 = SIMDString(simdstring2, 10, 10)
        simdstring6 = SIMDString(sample_string)
        simdstring8 = SIMDString(sample_string, 40)
        simdstring9 = SIMDString(sample_string, 4, 5)
        simdstring10 = SIMDString(10, "b")
        simdstring11 = SIMDString(simdstring10)

        self.compare_add("empty", simdstring0, 0, "")
        self.compare_add("char", simdstring1, 1, "a")
        self.compare_add(
            "string", simdstring2, 36, "0123456789abcdefghijklmnopqrstuvwxyz"
        )
        self.compare_add("substr", simdstring3, 26, "abcdefghijklmnopqrstuvwxyz")
        self.compare_add("substr with begin and end", simdstring4, 10, "abcdefghij")
        self.compare_add("sample string", simdstring6, 43, sample_string)
        self.compare_add("exclude string with substr", simdstring8, 3, "dog")
        self.compare_add(
            "substr with string with begin and end", simdstring9, 5, "quick"
        )
        self.compare_add("count with char", simdstring10, 10, "bbbbbbbbbb")

        simdstring10.insert(0, "01234566789")
        simdstring12 = SIMDString(simdstring10, 0, 5)

        self.compare_add("copy", simdstring11, 10, "bbbbbbbbbb")
        self.compare_add("insert and substr", simdstring12, 5, "01234")
