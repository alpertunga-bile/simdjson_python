from benchmark_base import BenchmarkBase

from simdstring import SIMDString

STR_LENGTH = 10
LONG_STR_LENGTH = 25


def string_append_op_char(count: int) -> None:
    string = ""

    for _ in range(count):
        string += "a"


def simd_append_op_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string += "a"


def simd_append_func_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.append("a")


def string_append_op_str(count: int) -> None:
    string = ""

    for _ in range(count):
        string += "a" * STR_LENGTH


def simd_append_op_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string += "a" * STR_LENGTH


def simd_append_func_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.append("a" * STR_LENGTH)


def string_append_op_long_str(count: int) -> None:
    string = ""

    for _ in range(count):
        string += "a" * LONG_STR_LENGTH


def simd_append_op_long_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string += "a" * LONG_STR_LENGTH


def simd_append_func_long_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.append("a" * LONG_STR_LENGTH)


class AppendBenchmarks(BenchmarkBase):
    def __init__(self) -> None:
        super().__init__()

        self.add_func(
            " Append Operation - Char (+=) ",
            [string_append_op_char, simd_append_op_char],
        )

        self.add_func(
            f"Append Operation - Str Length {STR_LENGTH} (+=)",
            [string_append_op_str, simd_append_op_str],
        )

        self.add_func(
            f"Append Operation - Str Length {LONG_STR_LENGTH} (+=)",
            [string_append_op_long_str, simd_append_op_long_str],
        )

        self.add_func(
            f"Append Function - Char",
            [string_append_op_char, simd_append_func_char],
        )

        self.add_func(
            f"Append Function - Str Length {STR_LENGTH}",
            [string_append_op_str, simd_append_func_str],
        )

        self.add_func(
            f"Append Function - Str Length {LONG_STR_LENGTH}",
            [string_append_op_long_str, simd_append_func_long_str],
        )


__all__ = [AppendBenchmarks]
