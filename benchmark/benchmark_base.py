from typing import Callable, Dict


class BenchmarkBase:
    funcs = Dict[str, list[Callable[[int], None]]]

    def __init__(self) -> None:
        self.funcs = {}

    def add_func(self, name: str, func: list[Callable[[int], None]]) -> None:
        self.funcs[name] = func
