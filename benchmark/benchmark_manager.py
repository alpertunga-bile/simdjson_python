from benchmark_base import BenchmarkBase
import timeit


class BenchmarkManager:
    log_file = "benchmark_results.log"
    COUNT = 1_000_000

    def __init__(self, count: int = 1_000_000) -> None:
        file = open(self.log_file, "w")

        print(f"Number of iterations : {self.COUNT}")
        file.write(f"Number of iterations : {self.COUNT}\n")
        file.close()

        self.COUNT = count

    def __print_time(self, name: str, func, count: int, file) -> None:
        start = timeit.default_timer()
        func(count)
        end = timeit.default_timer()

        name_str = "{0:20} |".format(name)

        print(f"{name_str} Elapsed Time : {end - start}")
        file.write(f"{name_str} Elapsed Time : {end - start}\n")

    def checkout_benchmark(self, benchmark: BenchmarkBase) -> None:
        file = open(self.log_file, "a")

        for func_name, func_list in benchmark.funcs.items():
            printable_string = func_name.center(100, "-")

            print(printable_string)
            file.write(printable_string + "\n")

            self.__print_time("Default String", func_list[0], self.COUNT, file)
            self.__print_time("SIMDString", func_list[1], self.COUNT, file)

            print("-" * 100)
            file.write("-" * 100 + "\n")

        file.close()
