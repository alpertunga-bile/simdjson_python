from test_base import TestBase

from simdstring import SIMDString

from utility import sample_string


class ContainsTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Contains Tests "

    def start(self) -> None:
        simdstring1 = SIMDString(sample_string)

        self.add("contains", simdstring1.contains("the") == True)
        self.add("contains 2", simdstring1.contains("woah") == False)
        self.add("contains 3", simdstring1.contains("T") == False)
