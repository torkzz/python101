"""
TestSubject class used for Unit Testing demonstration.
"""

class TestSubject:
    def add_values(self, a: int, b: int) -> int:
        """Return sum of two integers."""
        return a + b

    def combine_strings(self, *args: str) -> str:
        """Join positional string arguments with spaces and convert to UPPERCASE."""
        return " ".join(args).upper()
