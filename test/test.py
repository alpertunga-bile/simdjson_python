import sys
from os.path import join, exists
from os import getcwd

BUILT_PACKAGE_PATH = join(getcwd(), "build")

if exists(BUILT_PACKAGE_PATH) is False:
    print(f"{BUILT_PACKAGE_PATH} is not exists. Build the package first")
    exit(1)

sys.path.append(join(BUILT_PACKAGE_PATH, "Release"))
sys.path.append(join(BUILT_PACKAGE_PATH))

import simdstring

from test_manager import TestManager

from test_ctor import CtorTests

if __name__ == "__main__":
    manager = TestManager()

    ctor_test = CtorTests()

    manager.checkout_test(ctor_test)

    manager.finish()
