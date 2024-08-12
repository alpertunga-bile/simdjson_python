from benchmark_base import BenchmarkBase

from simdstring import SIMDString

STR_LENGTH = 10
LONG_STR_LENGTH = 25


def string_assign_char(count: int) -> None:
    string = ""

    for _ in range(count):
        string = "a"


def simd_assign_func_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.assign(1, "a")


def simd_assign_op_char(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string = "a"


def string_assign_str(count: int) -> None:
    string = ""

    for _ in range(count):
        string = "a" * STR_LENGTH


def simd_assign_func_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.assign(STR_LENGTH, "a")


def simd_assign_op_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string = "a" * STR_LENGTH


def string_assign_long_str(count: int) -> None:
    string = ""

    for _ in range(count):
        string = "a" * LONG_STR_LENGTH


def simd_assign_func_long_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string.assign(LONG_STR_LENGTH, "a")


def simd_assign_op_long_str(count: int) -> None:
    string = SIMDString()

    for _ in range(count):
        string = "a" * LONG_STR_LENGTH


class AssignBenchmarks(BenchmarkBase):
    def __init__(self) -> None:
        super().__init__()

        self.add_func(
            "Assign Function - Char", [string_assign_char, simd_assign_func_char]
        )

        self.add_func(
            "Assign Operation - Char", [string_assign_char, simd_assign_op_char]
        )

        self.add_func(
            f"Assign Function - String Length {STR_LENGTH}",
            [string_assign_str, simd_assign_func_str],
        )

        self.add_func(
            f"Assign Operation - String Length {STR_LENGTH}",
            [string_assign_str, simd_assign_op_str],
        )

        self.add_func(
            f"Assign Function - String Length {LONG_STR_LENGTH}",
            [string_assign_long_str, simd_assign_func_long_str],
        )

        self.add_func(
            f"Assign Operation - String Length {LONG_STR_LENGTH}",
            [string_assign_long_str, simd_assign_op_long_str],
        )


__all__ = [AssignBenchmarks]
