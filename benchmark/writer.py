from enum import Enum


class IWriter:
    _filename: str = None

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def start(self) -> None:
        file = open(self._filename, "w")
        file.close()

    def write_line(self, line: str) -> None:
        raise NotImplementedError


class LogWriter(IWriter):
    def __init__(self, filename: str) -> None:
        super().__init__(filename + ".log")

    def write_line(self, line: str) -> None:
        with open(self._filename, "a") as file:
            file.write(line + "\n")


class MarkdownHeaderOrientation(Enum):
    CENTER = 0
    LEFT = 1
    RIGHT = 2


class MarkdownWriter(IWriter):
    def __init__(self, filename: str) -> None:
        super().__init__(filename + ".md")

    def start(self) -> None:
        with open(self._filename, "w") as file:
            file.write("# SIMDString Benchmark Results\n\n")

    def start_table(
        self, headers: list[str], orientations: list[MarkdownHeaderOrientation]
    ) -> None:
        with open(self._filename, "w") as file:
            file.write("| ")

            for header in headers:
                file.write(header + " | ")

            file.write("\n| ")

            for orient in orientations:
                if orient == MarkdownHeaderOrientation.CENTER:
                    file.write(":-------: | ")
                elif orient == MarkdownHeaderOrientation.LEFT:
                    file.write(":-------- | ")
                elif orient == MarkdownHeaderOrientation.RIGHT:
                    file.write("--------: | ")

            file.write("\n")

    def write_line(self, line: str) -> None:
        with open(self._filename, "a") as file:
            file.write(f"- {line}\n\n")

    def write_table_row(self, lines: list[str]) -> None:
        with open(self._filename, "a") as file:
            file.write("| ")

            for line in lines:
                file.write(line + " | ")

            file.write("\n")
