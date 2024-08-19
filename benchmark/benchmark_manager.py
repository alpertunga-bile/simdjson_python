from benchmark_base import BenchmarkBase
import timeit

from writer import LogWriter, MarkdownWriter, MarkdownHeaderOrientation


class BenchmarkManager:
    _log_writer = LogWriter("benchmark_results")
    _md_writer = MarkdownWriter("benchmark_results")
    COUNT = 1_000_000

    def __init__(self, count: int = 1_000_000) -> None:
        self._log_writer.start()
        self._md_writer.start()

        print(f"Number of iterations : {self.COUNT}")
        self._log_writer.write_line(f"Number of iterations : {self.COUNT}")
        self._md_writer.write_line(f"Number of iterations : {self.COUNT}")

        self.COUNT = count

    def __print_time(self, name: str, func, count: int) -> float:
        start = timeit.default_timer()
        func(count)
        end = timeit.default_timer()

        name_str = "{0:20} |".format(name)

        print(f"{name_str} Elapsed Time : {end - start}")
        self._log_writer.write_line(f"{name_str} Elapsed Time : {end - start}")

        return end - start

    def checkout_benchmark(self, benchmark: BenchmarkBase) -> None:
        self._md_writer.start_table(
            ["Functions", "Default String", "SIMDString"],
            [
                MarkdownHeaderOrientation.LEFT,
                MarkdownHeaderOrientation.RIGHT,
                MarkdownHeaderOrientation.RIGHT,
            ],
        )

        for func_name, func_list in benchmark.funcs.items():
            printable_string = func_name.center(100, "-")

            print(printable_string)
            self._log_writer.write_line(printable_string)

            default_str_elapsed_time = self.__print_time(
                "Default String", func_list[0], self.COUNT
            )
            simdstring_elapsed_time = self.__print_time(
                "SIMDString", func_list[1], self.COUNT
            )

            self._md_writer.write_table_row(
                [
                    func_name,
                    "{0:3.15f}".format(default_str_elapsed_time),
                    "{0:3.15f}".format(simdstring_elapsed_time),
                ]
            )

            print("-" * 100)
            self._log_writer.write_line("-" * 100)

        self._md_writer.write_line(line="\n", start_prefix="")
