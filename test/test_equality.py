from test_base import TestBase

from simdstring import SIMDString


class EqualityTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Equality Tests "

    def start(self) -> None:
        simdstring1 = SIMDString(5, "a")
        simdstring2 = SIMDString(6, "a")
        simdstring3 = SIMDString(6, "b")
        simdstring4 = SIMDString(5, "a")

        string1 = "a" * 5
        string2 = "a" * 6
        string3 = "b" * 6

        self.add("self", simdstring1 == simdstring1)
        self.add("self 2", simdstring2 == simdstring2)
        self.add("self 3", simdstring3 == simdstring3)
        self.add("SIMDString", simdstring1 == simdstring4)

        self.add("SIMDString not", simdstring1 != simdstring2)
        self.add("SIMDString not 2", simdstring2 != simdstring1)

        self.add("SIMDString not 3", simdstring3 != simdstring2)
        self.add("SIMDString not 4", simdstring3 != simdstring2)

        self.add("SIMDString not 5", simdstring3 != simdstring1)
        self.add("SIMDString not 6", simdstring3 != simdstring1)

        self.add("string", simdstring1 == string1)
        self.add("string 2", simdstring2 == string2)
        self.add("string 3", simdstring3 == string3)

        self.add("string not", simdstring1 != string2)
        self.add("string not 2", simdstring2 != string1)

        self.add("string not 3", simdstring3 != string2)
        self.add("string not 4", simdstring2 != string3)

        self.add("string not 5", simdstring1 != string3)
        self.add("string not 6", simdstring3 != string1)

        self.add("empty", simdstring3 != "")
