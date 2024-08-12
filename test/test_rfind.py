from test_base import TestBase

from utility import find_test_string, find_test_string2, find_test_string3, check_result

from simdstring import SIMDString


def str_rfind(string: str, substr: str, pos: int) -> int:
    temp_str = string[: min(len(string) - len(substr), pos)][::-1]
    return len(temp_str) - temp_str.find(substr[::-1])


class RFindTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " RFind Tests "

    def start(self) -> None:
        string1 = find_test_string
        simdstring1 = SIMDString(find_test_string)
        substr = "abc"
        subsimdstr = SIMDString("abc")

        self.add(
            "substr", string1.rfind("abc") == check_result(simdstring1.rfind("abc"))
        )
        self.add(
            "substr 2", string1.rfind("abcd") == check_result(simdstring1.rfind("abcd"))
        )
        self.add(
            "substr 3",
            string1.rfind(substr) == check_result(simdstring1.rfind(subsimdstr)),
        )

        self.add(
            "substr w pos",
            str_rfind(string1, "abc", 10) == check_result(simdstring1.rfind("abc", 10)),
        )
        self.add(
            "substr w pos 2",
            str_rfind(string1, "abcd", 10)
            == check_result(simdstring1.rfind("abcd", 10)),
        )
        self.add(
            "substr w pos 3",
            str_rfind(string1, substr, 10)
            == check_result(simdstring1.rfind(subsimdstr, 10)),
        )

        self.add(
            "substr w pos 4",
            str_rfind(string1, "abc", 30) == check_result(simdstring1.rfind("abc", 30)),
        )
        self.add(
            "substr w pos 5",
            str_rfind(string1, "abcd", 30)
            == check_result(simdstring1.rfind("abcd", 30)),
        )
        self.add(
            "substr w pos 6",
            str_rfind(string1, substr, 30)
            == check_result(simdstring1.rfind(subsimdstr, 30)),
        )

        self.add("char", string1.rfind("c") == check_result(simdstring1.rfind("c")))
        self.add("char 2", string1.rfind("d") == check_result(simdstring1.rfind("d")))
        self.add("char 3", string1.rfind("A") == check_result(simdstring1.rfind("A")))

        self.add(
            "char with pos",
            str_rfind(string1, "c", 10) == check_result(simdstring1.rfind("c", 10)),
        )
        self.add(
            "char with pos 2",
            str_rfind(string1, "d", 10) == check_result(simdstring1.rfind("d", 10)),
        )
        self.add(
            "char with pos 3",
            str_rfind(string1, "A", 10) == check_result(simdstring1.rfind("A", 10)),
        )

        self.add(
            "char with pos 4",
            str_rfind(string1, "c", 30) == check_result(simdstring1.rfind("c", 30)),
        )
        self.add(
            "char with pos 5",
            str_rfind(string1, "d", 30) == check_result(simdstring1.rfind("d", 30)),
        )
        self.add(
            "char with pos 6",
            str_rfind(string1, "A", 30) == check_result(simdstring1.rfind("A", 30)),
        )

        self.add(
            "whole string",
            string1.rfind(find_test_string)
            == check_result(simdstring1.rfind(find_test_string)),
        )

        self.add(
            "whole string no match",
            string1.rfind(find_test_string2)
            == check_result(simdstring1.rfind(find_test_string2)),
        )
        self.add(
            "whole string no match 2",
            string1.rfind(find_test_string3)
            == check_result(simdstring1.rfind(find_test_string3)),
        )

        string2 = find_test_string[:30]
        simdstring2 = SIMDString(find_test_string, 30)

        self.add(
            "edge case out of scope",
            str_rfind(string2, "d", 6) == check_result(simdstring2.rfind("d", 6)),
        )
        self.add(
            "edge case out of scope 2",
            str_rfind(string2, "cd", 6) == check_result(simdstring2.rfind("cd", 6)),
        )
        self.add(
            "edge case out of scope 3",
            str_rfind(string2, "d", len(string2))
            == check_result(simdstring2.rfind("d", len(simdstring2))),
        )
        self.add(
            "edge case out of scope 4",
            str_rfind(string2, "cd", len(string2))
            == check_result(simdstring2.rfind("cd", len(simdstring2))),
        )

        simdstring3 = SIMDString()
        string3 = ""

        self.add(
            "empty string", string3.rfind("a") == check_result(simdstring3.rfind("a"))
        )
        self.add(
            "empty string 2",
            string3.rfind("abcd") == check_result(simdstring3.rfind("abcd")),
        )

        simdstring4 = SIMDString("test")
        simdstring4 += "\0"
        simdstring4 += "null"

        string4 = "test"
        string4 += "\0"
        string4 += "null"

        self.add(
            "edge case null char",
            string4.rfind("\0") == check_result(simdstring4.rfind("\0")),
        )
