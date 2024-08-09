from test_base import TestBase

from utility import find_test_string, find_test_string2, find_test_string3, check_result

from simdstring import SIMDString


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

        test = string1.rfind("abc", 10)
        test_2 = simdstring1.rfind("abc", 10)

        self.add(
            "substr w pos",
            string1.rfind("abc", 10) == check_result(simdstring1.rfind("abc", 10)),
        )
        self.add(
            "substr w pos 2",
            string1.rfind("abcd", 10) == check_result(simdstring1.rfind("abcd", 10)),
        )
        self.add(
            "substr w pos 3",
            string1.rfind(substr, 10)
            == check_result(simdstring1.rfind(subsimdstr, 10)),
        )

        self.add(
            "substr w pos 4",
            string1.rfind("abc", 30) == check_result(simdstring1.rfind("abc", 30)),
        )
        self.add(
            "substr w pos 5",
            string1.rfind("abcd", 30) == check_result(simdstring1.rfind("abcd", 30)),
        )
        self.add(
            "substr w pos 6",
            string1.rfind(substr, 30)
            == check_result(simdstring1.rfind(subsimdstr, 30)),
        )
