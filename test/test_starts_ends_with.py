from test_base import TestBase

from simdstring import SIMDString

from utility import sample_string


class StartsEndsWithTests(TestBase):
    def __init__(self) -> None:
        super().__init__()
        self.base_test_name = " Starts Ends With "

    def start(self) -> None:
        simdstring1 = SIMDString(sample_string)

        self.add(
            "starts with",
            sample_string.startswith("the") == simdstring1.starts_with("the"),
        )
        self.add(
            "starts with 2",
            sample_string.startswith("woah") == simdstring1.starts_with("woah"),
        )
        self.add(
            "ends with", sample_string.endswith("dog") == simdstring1.ends_with("dog")
        )
        self.add(
            "ends with 2",
            sample_string.endswith("woah") == simdstring1.ends_with("woah"),
        )
        self.add(
            "starts with char",
            sample_string.startswith("t") == simdstring1.starts_with("t"),
        )
        self.add(
            "starts with char 2",
            sample_string.startswith("w") == simdstring1.starts_with("w"),
        )
        self.add(
            "ends with char", sample_string.endswith("g") == simdstring1.ends_with("g")
        )
        self.add(
            "ends with char 2",
            sample_string.endswith("h") == simdstring1.ends_with("h"),
        )
        self.add(
            "starts with self",
            sample_string.startswith(sample_string)
            == simdstring1.starts_with(sample_string),
        )
        self.add(
            "ends with self",
            sample_string.endswith(sample_string)
            == simdstring1.ends_with(sample_string),
        )

        self.add(
            "ends with substr",
            SIMDString("hello world"[6:]).ends_with("hello world") == False,
        )
