from test_base import TestBase

from utility import sample_string

from simdstring import SIMDString


def str_erase(string: str, pos: int, length: int) -> str:
    return string[:pos] + string[pos + length :]


class ClearEraseTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Clear Erase Tests "

    def start(self) -> None:
        simdstring1 = SIMDString(sample_string)
        string1 = sample_string

        string1 = str_erase(string1, 6, 12)
        simdstring1.erase(6, 12)

        self.compare_add("erase", simdstring1, len(string1), string1)

        simdstring2 = SIMDString(sample_string)
        simdstring2.clear()

        self.add(
            "clear",
            simdstring2.size() == 0
            and len(simdstring2) == 0
            and simdstring2.value == ""
            and simdstring2.empty == True,
        )

        simdstring3 = SIMDString(sample_string)
        string3 = sample_string

        string3 = str_erase(string3, 10, 1)
        simdstring3.erase(10, 1)

        self.add(
            "erase 2",
            len(simdstring3) == len(string3)
            and simdstring3 == string3
            and simdstring3.is_empty() == False,
        )

        string4 = "a" * 100
        simdstring4 = SIMDString(100, "a")

        string4 = string4[:75] + "b" + string4[76:]
        simdstring4[75] = "b"

        self.add(
            "change with index op",
            len(simdstring4) == len(string4)
            and simdstring4 == string4
            and simdstring4.is_empty() == False,
        )
