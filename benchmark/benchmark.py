import sys
from os.path import join, exists
from os import getcwd

BUILT_PACKAGE_PATH = join(getcwd(), "build")

if exists(BUILT_PACKAGE_PATH) is False:
    print(f"{BUILT_PACKAGE_PATH} is not exists. Build the package first")
    exit(1)

sys.path.append(join(BUILT_PACKAGE_PATH, "Release"))
sys.path.append(BUILT_PACKAGE_PATH)

from benchmark_manager import BenchmarkManager
from benchmark_append import AppendBenchmarks

if __name__ == "__main__":
    manager = BenchmarkManager()

    append_bk = AppendBenchmarks()

    manager.checkout_benchmark(append_bk)
