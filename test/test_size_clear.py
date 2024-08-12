from test_base import TestBase

from simdstring import SIMDString

from utility import sample_string


class SizeClearTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Size Clear Tests "

    def start(self) -> None:
        simdstring1 = SIMDString(sample_string)
        string1 = sample_string

        simdstring1.resize(50)
        string1 = string1.ljust(50)

        self.add(
            "resize bigger",
            string1.strip() == simdstring1.value and len(simdstring1) == len(string1),
        )

        simdstring1.resize(60, "!")
        string1 = string1.ljust(60, "!")

        self.add(
            "resize bigger w char",
            string1 == simdstring1.value and len(simdstring1) == len(string1),
        )

        simdstring1.resize(40)
        string1 = string1[:40]

        self.add(
            "resize smaller",
            string1 == simdstring1.value and len(simdstring1) == len(string1),
        )

        self.add("length", len(simdstring1) == len(string1))

        self.add("empty", simdstring1.empty == False)

        simdstring1.clear()
        self.add("clear/empty", simdstring1.empty == True)
