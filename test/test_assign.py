from test_base import TestBase
from utility import sample_string

from simdstring import SIMDString


class AssignTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Assign Tests "

    def start(self) -> None:
        simdstring0 = SIMDString()

        self.compare_add("empty", simdstring0, 0, "")

        simdstring0.assign(1, "a")

        self.compare_add("char", simdstring0, 1, "a")

        simdstring1 = SIMDString(sample_string, 26)
        simdstring2 = SIMDString("0123456789abcdefghijklmnopqrstuvwxyz")

        simdstring0.assign(simdstring2)
        self.compare_add(
            "SIMDString", simdstring2, 36, "0123456789abcdefghijklmnopqrstuvwxyz"
        )

        simdstring0.assign(simdstring1, 16, 5)
        self.compare_add("substr with begin and size", simdstring0, 5, "fox j")

        simdstring0.assign(simdstring2, 10)
        self.compare_add("substr", simdstring0, 26, "abcdefghijklmnopqrstuvwxyz")

        simdstring0.assign(simdstring2, 10, 10)
        self.compare_add("substr with begin and size 2", simdstring0, 10, "abcdefghij")

        simdstring0 = SIMDString(sample_string)
        self.compare_add("SIMDString with string", simdstring0, 43, sample_string)

        simdstring0 = simdstring0
        self.compare_add("self", simdstring0, 43, sample_string)

        simdstring3 = SIMDString(100, "a")
        string3 = "a" * 100
        self.compare_add("char with count", simdstring3, len(string3), string3)

        simdstring0.assign(sample_string)
        self.compare_add("string", simdstring0, 43, sample_string)

        simdstring0.assign(simdstring2.value)
        self.compare_add(
            "with SIMDString class's value", simdstring0, len(simdstring2), simdstring2
        )

        string4 = "c" * 40
        simdstring0 = string4
        self.compare_add("string assing op", simdstring0, len(string4), string4)

        simdstring0 = ""
        self.compare_add("empty string", simdstring0, 0, "")
