from test_base import TestBase
from utility import sample_string

from simdstring import SIMDString


class CtorTests(TestBase):
    def start(self) -> None:
        self.base_test_name = " Constructor Tests "

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

        self.add("empty", len(simdstring0) == 0 and simdstring0 == "")
        self.add("char", len(simdstring1) == 1 and simdstring1 == "a")
        self.add(
            "string",
            len(simdstring2) == 36
            and simdstring2 == "0123456789abcdefghijklmnopqrstuvwxyz",
        )
        self.add(
            "substr",
            len(simdstring3) == 26 and simdstring3 == "abcdefghijklmnopqrstuvwxyz",
        )
        self.add(
            "substr with begin and end",
            len(simdstring4) == 10 and simdstring4 == "abcdefghij",
        )
        self.add(
            "sample string",
            len(simdstring6) == 43 and simdstring6 == sample_string,
        )
        self.add("substr with string", len(simdstring8) == 3 and simdstring8 == "dog")
        self.add(
            "substr with string with begin and end",
            len(simdstring9) == 5 and simdstring9 == "quick",
        )
        self.add(
            "count with char", len(simdstring10) == 10 and simdstring10 == "bbbbbbbbbb"
        )

        simdstring10.insert(0, "01234566789")
        simdstring12 = SIMDString(simdstring10, 0, 5)

        self.add("copy", len(simdstring11) == 10 and simdstring11 == "bbbbbbbbbb")
        self.add(
            "insert and substr", len(simdstring12) == 5 and simdstring12 == "01234"
        )
