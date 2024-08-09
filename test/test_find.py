from test_base import TestBase

from utility import find_test_string, find_test_string2, find_test_string3

from simdstring import SIMDString


class FindTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Find Tests "

    def start(self) -> None:
        string1 = find_test_string
        simdstring1 = SIMDString(find_test_string)
        substr = "abc"
        subsimdstr = "abc"

        def check_result(res: int) -> int:
            return res if res != 18446744073709551615 else -1

        self.add("substr", string1.find("abc") == simdstring1.find("abc"))
        self.add("substr 2", string1.find("abcd") == simdstring1.find("abcd"))
        self.add("substr string", string1.find(substr) == simdstring1.find(subsimdstr))

        self.add("substr pos", string1.find("abc", 10) == simdstring1.find("abc", 10))
        self.add(
            "substr pos 2", string1.find("abcd", 10) == simdstring1.find("abcd", 10)
        )
        self.add(
            "substr pos 3", string1.find(substr, 10) == simdstring1.find(subsimdstr, 10)
        )

        self.add("substr pos 3", string1.find("abc", 30) == simdstring1.find("abc", 30))

        self.add(
            "substr pos 4",
            string1.find("abcd", 30) == check_result(simdstring1.find("abcd", 30)),
        )

        self.add(
            "substr pos 5", string1.find(substr, 30) == simdstring1.find(subsimdstr, 30)
        )

        self.add("char", string1.find("a") == simdstring1.find("a"))
        self.add("char 2", string1.find("c") == simdstring1.find("c"))
        self.add("char 3", string1.find("d") == simdstring1.find("d"))
        self.add(
            "char 4",
            string1.find("4") == check_result(simdstring1.find("4")),
        )

        self.add(
            "whole string",
            string1.find(find_test_string) == simdstring1.find(find_test_string),
        )

        self.add(
            "whole string 2",
            string1.find(find_test_string2)
            == check_result(simdstring1.find(find_test_string2)),
        )

        self.add(
            "whole string 3",
            string1.find(find_test_string3)
            == check_result(simdstring1.find(find_test_string3)),
        )

        string2 = "a" * 20
        simdstring2 = SIMDString(20, "a")
        string2 = string2[:15] + "b" + string2[16:]
        simdstring2[15] = "b"
        string2 = string2[:11]
        simdstring2.resize(11)

        self.add(
            "edge case", string2.find("b", 6) == check_result(simdstring2.find("b", 6))
        )
        self.add(
            "edge case 2",
            string2.find("ab", 6) == check_result(simdstring2.find("ab", 6)),
        )
        self.add(
            "edge case 3",
            string2.find("b", len(string2))
            == check_result(simdstring2.find("b", len(simdstring2))),
        )
        self.add(
            "edge case 4",
            string2.find("ab", len(string2))
            == check_result(simdstring2.find("ab", len(simdstring2))),
        )

        self.add("empty string", string2.find("") == check_result(simdstring2.find("")))
        self.add(
            "empty string 2",
            string2.find("", 6) == check_result(simdstring2.find("", 6)),
        )
        self.add(
            "empty string 3",
            string2.find("", len(string2))
            == check_result(simdstring2.find("", len(simdstring2))),
        )

        string3 = ""
        simdstring3 = SIMDString()

        self.add("empty", string3.find("a") == check_result(simdstring3.find("a")))
        self.add(
            "empty 2", string3.find("abcd") == check_result(simdstring3.find("abcd"))
        )

        simdstring4 = SIMDString("test")
        simdstring4 += "\0"
        simdstring4 += "null"
        string4 = "test"
        string4 += "\0"
        string4 += "null"

        self.add(
            "edge case null char",
            string4.find("\0") == check_result(simdstring4.find("\0")),
        )
