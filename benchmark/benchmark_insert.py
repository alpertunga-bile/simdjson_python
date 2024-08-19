from benchmark_base import BenchmarkBase

from simdstring import SIMDString


def str_insert(string: str, index: int, insert_string: str) -> str:
    return string[:index] + insert_string + string[index:]


def string_insert_begin_char(count: int) -> None:
    string = ""

    for _ in range(count):
        string = "a" + string


def simdstring_insert_begin_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.insert(0, "a")


def string_insert_end_char(count: int) -> None:
    string = ""

    for _ in range(count):
        string = string + "a"


def simdstring_insert_end_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.insert(len(string), "a")


def string_insert_middle_char(count: int) -> None:
    string = ""

    for _ in range(count):
        string = str_insert(string, len(string) // 2, "a")


def simdstring_insert_middle_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.insert(len(string) // 2, "a")


def string_insert_begin_str(count: int) -> None:
    string = ""

    for _ in range(count):
        string = "abc" + string


def simdstring_insert_begin_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.insert(0, "abc")


class InsertBenchmarks(BenchmarkBase):
    def __init__(self) -> None:
        super().__init__()

        self.add_func(
            "Insert At The Beginning - Char",
            [string_insert_begin_char, simdstring_insert_begin_char],
        )

        self.add_func(
            "Insert At The End - Char",
            [string_insert_end_char, simdstring_insert_end_char],
        )

        self.add_func(
            "Insert In The Middle - Char",
            [string_insert_middle_char, simdstring_insert_middle_char],
        )


__all__ = [InsertBenchmarks]
