from test_base import TestBase

from utility import sample_string

from simdstring import SIMDString


class SwapTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Swap Tests "

    def start(self) -> None:
        string1 = "a" * 20
        simdstring1 = SIMDString(20, "a")

        string2 = sample_string
        simdstring2 = SIMDString(sample_string)

        string3 = "b" * 100
        simdstring3 = SIMDString(100, "b")

        simdstring1.swap(simdstring2)

        self.add(
            "swap",
            simdstring1 == string2
            and len(simdstring1) == len(string2)
            and simdstring2 == string1
            and len(simdstring2) == len(string1),
        )

        simdstring1.swap(simdstring3)

        self.add(
            "swap 2",
            simdstring1 == string3
            and len(simdstring1) == len(string3)
            and simdstring3 == string2
            and len(simdstring3) == len(string2),
        )
