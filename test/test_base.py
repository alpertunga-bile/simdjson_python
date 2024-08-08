from typing import Dict


class TestBase:
    base_test_name: str = None
    results: Dict[str, bool] = {}

    def __init__(self) -> None:
        self.base_test_name = None
        self.results = {}

    def start(self) -> None:
        return NotImplementedError

    def add(self, test_name: str, test_result: bool) -> None:
        self.results[test_name] = test_result

    def compare_add(
        self, test_name: str, result: str, wanted_size: int, wanted_result: str
    ) -> None:
        test_result = len(result) == wanted_size and result == wanted_result

        self.add(test_name, test_result)
