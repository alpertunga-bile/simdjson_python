from typing import Dict


class TestBase:
    base_test_name: str = None
    results: Dict[str, bool] = {}

    def start(self) -> None:
        return NotImplementedError

    def add(self, test_name: str, test_result: bool) -> None:
        self.results[test_name] = test_result

    def compare_add(
        self, test_name: str, first_result: str, second_result: str
    ) -> None:
        test_result = first_result == second_result

        self.add(test_name, test_result)
