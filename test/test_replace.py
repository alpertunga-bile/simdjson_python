from test_base import TestBase

from simdstring import SIMDString


def str_replace(string: str, pos: int, length: int, replace_string: str) -> str:
    return string[:pos] + replace_string + string[pos + length :]


def str_replace_w_substr(
    string: str, pos: int, length: int, replace_string: str, subpos: int, sublen: int
) -> str:
    return str_replace(string, pos, length, replace_string[subpos : subpos + sublen])


def str_replace_w_n(
    string: str, pos: int, length: int, replace_string: str, n: int
) -> str:
    return str_replace(string, pos, length, replace_string[:n])


def str_replace_w_count(
    string: str, pos: int, length: int, n: int, replace_string: str
) -> str:
    return str_replace(string, pos, length, replace_string * n)


class ReplaceTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Replace Tests "

    def __add_replace_test(
        self, name: str, std_pos: int, simd_pos: int, count: int, count2: int
    ) -> None:
        string1 = "0123456789"
        string2 = "abcdefg"

        simdstring1 = SIMDString("0123456789")
        simdstring2 = SIMDString("abcdefg")

        string1 = str_replace(string1, std_pos, count, string2)
        simdstring1 = simdstring1.replace(simd_pos, count, simdstring2)

        self.compare_add(name, simdstring1, len(string1), string1)

        string1 = str_replace_w_substr(string1, std_pos, count, string2, 2, count2)
        simdstring1 = simdstring1.replace(simd_pos, count, simdstring2, 2, count2)

        self.compare_add(f"{name} 1", simdstring1, len(string1), string1)

        string1 = str_replace(string1, std_pos, count, "hijklmnop")
        simdstring1.replace(simd_pos, count, "hijklmnop")

        self.compare_add(f"{name} 2", simdstring1, len(string1), string1)

        string1 = str_replace_w_n(string1, std_pos, count, "hijklmnop", count2)
        simdstring1.replace(simd_pos, count, "hijklmnop", count2)

        self.compare_add(f"{name} 3", simdstring1, len(string1), string1)

        string1 = str_replace_w_count(string1, std_pos, count, count2, "z")
        simdstring1.replace(simd_pos, count, count2, "z")

        self.compare_add(f"{name} 4", simdstring1, len(string1), string1)

    def start(self) -> None:
        string1 = "0123456789"
        simdstring1 = SIMDString("0123456789")

        self.__add_replace_test("beginning grow", 0, 0, 1, 4)
        self.__add_replace_test("beginning shrink", 0, 0, 10, 4)
        self.__add_replace_test("beginning same size", 0, 0, 5, 5)

        self.__add_replace_test("middle grow", 5, 5, 1, 4)
        self.__add_replace_test("middle shrink", 5, 5, 10, 4)
        self.__add_replace_test("middle same size", 5, 5, 5, 5)

        self.__add_replace_test(
            "near the end grow", len(string1) - 1, len(simdstring1) - 1, 1, 4
        )
        self.__add_replace_test(
            "near the end shrink", len(string1) - 1, len(simdstring1) - 1, 10, 4
        )
        self.__add_replace_test(
            "near the end same size", len(string1) - 1, len(simdstring1) - 1, 5, 5
        )

        self.__add_replace_test("end grow", len(string1), len(simdstring1), 1, 4)
        self.__add_replace_test("end shrink", len(string1), len(simdstring1), 10, 4)
        self.__add_replace_test("end same size", len(string1), len(simdstring1), 5, 5)

        string3 = "abcdefg"
        simdstring3 = SIMDString("abcdefg")

        string3 = str_replace(string3, 0, len(string1), string1)
        simdstring3.replace(0, len(simdstring1), simdstring1)

        self.compare_add("buffer to heap", simdstring3, len(string3), string3)
