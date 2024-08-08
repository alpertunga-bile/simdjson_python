from test_base import TestBase

from utility import sample_string

from simdstring import SIMDString


class AccessTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Access Tests "

    def start(self) -> None:
        simdstring = SIMDString(sample_string)

        self.add("at", simdstring.at(4) == "q")
        self.add("operator[]", simdstring[4] == "q")
        self.add("front", simdstring.front() == "t")
        self.add("back", simdstring.back() == "g")
        self.add("value", simdstring.value == sample_string)
        self.add("data", simdstring.data() == sample_string)

        a_string = "aaaaa"
        const_string1 = "baaaa"
        const_string2 = "abaaa"
        const_string3 = "aabaa"
        const_string4 = "aaaab"

        simdstring2 = SIMDString(const_string2)
        simdstring2[1] = "a"
        self.add(
            "operator[] assign",
            simdstring2 != const_string2 and simdstring2 == a_string,
        )
