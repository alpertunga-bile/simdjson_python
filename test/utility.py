sample_string = "the quick brown fox jumps over the lazy dog"
sample_string_size = len(sample_string)
sample_string_large = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
find_test_string = "abcabcabcabcabcabcabcdabcabcABCabc"
find_test_string2 = "abcabcabcabcabcabcabcdabcabcabcabcadsf"
find_test_string3 = "abcabcabcabcabcabcabcabcabcABCabc"


def check_result(res: int) -> int:
    return res if res != 18446744073709551615 else -1
