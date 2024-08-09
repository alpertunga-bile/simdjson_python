from test_base import TestBase

from utility import sample_string

from simdstring import SIMDString


class AppendTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Append Tests "

    def start(self) -> None:
        string1 = "a" * 5
        string2 = "b" * 6

        simdstring1 = SIMDString(5, "a")
        simdstring2 = SIMDString(6, "b")

        self.add("add op string", (string1 + "abc") == (simdstring1 + "abc"))
        self.add("add op char", (string1 + "a") == (simdstring1 + "a"))

        string1 += string2[:2]
        simdstring1.append(string2[:2])

        self.compare_add("append w pos", string1, len(string1), simdstring1)

        string1 += string2[2:4]
        simdstring1.append(string2[2:4])

        self.compare_add("append w pos and count", string1, len(string1), simdstring1)

        string1 += "0123456789"
        simdstring1.append("0123456789")

        self.compare_add("string", string1, len(string1), simdstring1)

        string1 += sample_string
        simdstring1.append(sample_string)

        self.compare_add("string 2", string1, len(string1), simdstring1)

        string1 += " " * 6
        simdstring1.append(6, " ")

        self.compare_add("string w count", string1, len(string1), simdstring1)

        self.add("concat", (string1 + string2) == (simdstring1 + simdstring2))
        self.add("concat 2", (string1 + sample_string) == (simdstring1 + sample_string))
        self.add("concat char", (string1 + "a") == (simdstring1 + "a"))
        self.add("concat 3", (sample_string + string1) == (sample_string + simdstring1))
        self.add("concat char", ("a" + string1) == ("a" + simdstring1))
