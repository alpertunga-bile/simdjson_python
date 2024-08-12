import sys
from os.path import join, exists
from os import getcwd

BUILT_PACKAGE_PATH = join(getcwd(), "build")

if exists(BUILT_PACKAGE_PATH) is False:
    print(f"{BUILT_PACKAGE_PATH} is not exists. Build the package first")
    exit(1)

sys.path.append(join(BUILT_PACKAGE_PATH, "Release"))
sys.path.append(BUILT_PACKAGE_PATH)

from test_manager import TestManager
from test_ctor import CtorTests
from test_assign import AssignTests
from test_access import AccessTests
from test_equality import EqualityTests
from test_append import AppendTests
from test_push_pop import PushPopTests
from test_insert import InsertTests
from test_replace import ReplaceTests
from test_clear_erase import ClearEraseTests
from test_swap import SwapTests
from test_find import FindTests
from test_rfind import RFindTests
from test_find_first_last_of import FindFirstLastOfTests
from test_starts_ends_with import StartsEndsWithTests
from test_contains import ContainsTests

if __name__ == "__main__":
    manager = TestManager()

    ctor_test = CtorTests()
    assign_test = AssignTests()
    access_test = AccessTests()
    equality_test = EqualityTests()
    append_test = AppendTests()
    push_pop_test = PushPopTests()
    insert_test = InsertTests()
    replace_test = ReplaceTests()
    clear_erase_test = ClearEraseTests()
    swap_test = SwapTests()
    find_test = FindTests()
    rfind_test = RFindTests()
    find_first_last_of_test = FindFirstLastOfTests()
    start_end_with_test = StartsEndsWithTests()
    contain_test = ContainsTests()

    manager.checkout_test(ctor_test)
    manager.checkout_test(assign_test)
    manager.checkout_test(access_test)
    manager.checkout_test(equality_test)
    manager.checkout_test(append_test)
    manager.checkout_test(push_pop_test)
    manager.checkout_test(insert_test)
    manager.checkout_test(replace_test)
    manager.checkout_test(clear_erase_test)
    manager.checkout_test(swap_test)
    manager.checkout_test(find_test)
    manager.checkout_test(rfind_test)
    manager.checkout_test(find_first_last_of_test)
    manager.checkout_test(start_end_with_test)
    manager.checkout_test(contain_test)

    manager.finish()
