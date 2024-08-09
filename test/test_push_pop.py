from test_base import TestBase

from utility import sample_string

from simdstring import SIMDString


class PushPopTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " PushPopTests "

    def start(self) -> None:
        simdstring1 = SIMDString(sample_string)
        string1 = sample_string

        string1 += "a"
        simdstring1.push_back("a")

        self.compare_add("push_back", simdstring1, len(string1), string1)

        string1 = sample_string
        simdstring1.pop_back()

        self.compare_add("pop_back", simdstring1, len(string1), string1)

        simdstring2 = SIMDString()
        simdstring2.push_back("a")

        self.compare_add("empty push_back", simdstring2, 1, "a")
