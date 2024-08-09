from test_base import TestBase


class TestManager:
    correct_result_counter = 0
    total_tests = 0
    log_file = "test_results.log"

    def __init__(self) -> None:
        file = open(self.log_file, "w")
        file.close()

    def checkout_test(self, test: TestBase) -> None:
        test.start()

        file = open(self.log_file, "a")

        printable_string = test.base_test_name.center(100, "-")

        print(printable_string)
        file.write(printable_string + "\n")

        for name, result in test.results.items():
            self.total_tests += 1

            if result:
                self.correct_result_counter += 1

            printable_string = "{0:50} {1:10}".format(
                name, "Passed" if result else "Failed"
            )

            print(printable_string)

            file.write(printable_string + "\n")

        print("-" * 100)
        file.write("-" * 100 + "\n")

        file.close()

    def finish(self) -> None:
        file = open(self.log_file, "a")

        printable_string = "{0:50} {1}\n".format("Total Tests", self.total_tests)
        printable_string += "{0:50} {1}\n".format(
            "Passed Tests", self.correct_result_counter
        )
        printable_string += "{0:50} %{1:3.2f}".format(
            "Passed Ratio", self.correct_result_counter / self.total_tests * 100.0
        )

        print(printable_string)
        file.write(printable_string + "\n")

        file.close()
