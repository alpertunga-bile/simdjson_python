from test_base import TestBase

from simdstring import SIMDString


def str_insert(string: str, index: int, insert_string: str) -> str:
    return string[:index] + insert_string + string[index:]


def str_insert_w_len(
    string: str, index: int, insert_string: str, subpos: int, sublen: int
) -> str:
    return str_insert(string, index, insert_string[subpos : subpos + sublen])


def str_insert_w_n(string: str, index: int, insert_string: str, n: int):
    return str_insert(string, index, insert_string[:n])


def str_insert_w_count(string: str, index: int, count: int, insert_string: str):
    return str_insert(string, index, insert_string * count)


class InsertTests(TestBase):

    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Insert Tests "

    def __insert_test(self, name: str, std_pos: int, simd_pos: int) -> None:
        string1 = "0123456789"
        string2 = "abcdefg"
        simdstring1 = SIMDString("0123456789")
        simdstring2 = SIMDString("abcdefg")

        string1 = str_insert(string1, std_pos, string2)
        simdstring1.insert(simd_pos, simdstring2)

        self.compare_add(name, simdstring1, len(string1), string1)

        string1 = str_insert_w_len(string1, std_pos, string2, 2, 3)
        simdstring1.insert(simd_pos, simdstring2, 2, 3)

        self.compare_add(f"{name} 1", simdstring1, len(string1), string1)

        string1 = str_insert(string1, std_pos, "hijklmnop")
        simdstring1.insert(simd_pos, "hijklmnop")

        self.compare_add(f"{name} 2", simdstring1, len(string1), string1)

        string1 = str_insert_w_n(string1, std_pos, "hijklmnop", 4)
        simdstring1.insert(simd_pos, "hijklmnop", 4)

        self.compare_add(f"{name} 3", simdstring1, len(string1), string1)

        string1 = str_insert_w_count(string1, std_pos, 6, "z")
        simdstring1.insert(simd_pos, 6, "z")

        self.compare_add(f"{name} 4", simdstring1, len(string1), string1)

    def start(self) -> None:
        string1 = "0123456789"
        simdstring1 = SIMDString("0123456789")

        self.__insert_test("beginning", 0, 0)
        self.__insert_test("middle", int(len(string1) / 2), int(len(simdstring1) / 2))
        self.__insert_test("near the end", len(string1) - 1, len(simdstring1) - 1)
