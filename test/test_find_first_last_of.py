from test_base import TestBase

from utility import check_result

from simdstring import SIMDString


def str_find_first_of(string: str, chars: str, pos: int = 0) -> int:
    temp_str = string[min(pos, 0) :]
    idx = len(temp_str) + 1

    for c in chars:
        c_idx = temp_str.find(c)

        if c_idx != -1:
            idx = min(c_idx + pos, idx)

    return -1 if idx == len(temp_str) + 1 else idx


def str_find_last_of(string: str, chars: str, pos: int = -1) -> int:
    calc_pos = pos if pos != -1 else len(string)
    temp_str = string[: min(calc_pos + 1, len(string))]
    idx = -1

    for c in chars:
        c_idx = temp_str.rfind(c)

        if c_idx != -1:
            idx = max(c_idx, idx)

    return idx


class FindFirstLastOfTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Find First Last Of Tests "

    def start(self) -> None:
        find_first_last_of_test_string = "The quick brown fox jumps over the lazy dog. Sphinx of black quartz, judge my vow."
        string1 = find_first_last_of_test_string
        simdstring1 = SIMDString(find_first_last_of_test_string)

        self.add(
            "char",
            str_find_first_of(string1, "d")
            == check_result(simdstring1.find_first_of("d")),
        )
        self.add(
            "substr",
            str_find_first_of(string1, "mnop")
            == check_result(simdstring1.find_first_of("mnop")),
        )
        self.add(
            "char 2",
            str_find_last_of(string1, "d")
            == check_result(simdstring1.find_last_of("d")),
        )
        self.add(
            "substr 2",
            str_find_last_of(string1, "mnop")
            == check_result(simdstring1.find_last_of("mnop")),
        )

        self.add(
            "char w pos",
            str_find_first_of(string1, "d", 40)
            == check_result(simdstring1.find_first_of("d", 40)),
        )
        self.add(
            "substr w pos",
            str_find_first_of(string1, "mnop", 40)
            == check_result(simdstring1.find_first_of("mnop", 40)),
        )
        self.add(
            "char w pos 2",
            str_find_last_of(string1, "d", 40)
            == check_result(simdstring1.find_last_of("d", 40)),
        )
        self.add(
            "substr w pos 2",
            str_find_last_of(string1, "mnop", 40)
            == check_result(simdstring1.find_last_of("mnop", 40)),
        )

        self.add(
            "edge case match == pos",
            str_find_first_of(string1, "q", string1.find("q"))
            == simdstring1.find_first_of("q", simdstring1.find("q")),
        )
