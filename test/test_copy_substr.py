from test_base import TestBase

from simdstring import SIMDString


class CopySubstrTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Copy Substr Tests "

    def start(self) -> None:
        copy_substr_test_string = "0123456789abcdefghijklmnopqrstuvwxyz"
        simdstring1 = SIMDString(copy_substr_test_string)
        temp = "a" * 11
        temp = temp[:9] + "\0" + temp[10:]

        simdstring1.copy(temp, 10)

        self.compare_add("copy", temp, 10, "0123456789")

        substr = SIMDString(simdstring1.substr(0, 10))

        self.compare_add("substr", substr, 10, "0123456789")

        substr = simdstring1.substr(10)
        self.compare_add(
            "substr 2",
            substr,
            len(copy_substr_test_string[10:]),
            copy_substr_test_string[10:],
        )

        simdstring2 = SIMDString("test")
        simdstring2 += "\0"
        simdstring2 += "null"
        simdstring2 += "\0"
        simdstring2 += "ability"

        substr = simdstring2.substr(10)
        self.add(
            "substr with null chars",
            "ability" == substr and len(substr) == (len(simdstring2) - 10),
        )
