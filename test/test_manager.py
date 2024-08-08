from dataclasses import dataclass
from test_base import TestBase


@dataclass
class TestManager:
    correct_result_counter = 0
    total_tests = 0

    def checkout_test(self, test: TestBase) -> None:
        test.start()

        print(test.base_test_name.center(100, "-"))

        for name, result in test.results.items():
            self.total_tests += 1

            if result:
                self.correct_result_counter += 1

            print("{0:50} {1:10}".format(name, "Passed" if result else "Failed"))

        print("-" * 100)

    def finish(self) -> None:
        print(
            "{0:50} %{1:3.2f}".format(
                "Passed Ratio", self.correct_result_counter / self.total_tests * 100.0
            )
        )
