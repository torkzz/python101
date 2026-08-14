"""
Unit Testing in Python using `unittest`

Concepts:
- Standard `unittest` framework.
- `unittest.TestCase` base class.
- Test assertion methods (`assertEqual`, `assertNotEqual`).
- Custom failure messages in assertions.
- Running tests with `unittest.main()`.
"""

import unittest
from testsubject import TestSubject


class TestMySubject(unittest.TestCase):

    def test_added_values_correct(self):
        t = TestSubject()
        v = t.add_values(5, 3)
        self.assertEqual(v, 8)

    def test_added_values_incorrect(self):
        t = TestSubject()
        v = t.add_values(5, 3)
        self.assertNotEqual(v, 9)

    def test_combined_strings(self):
        t = TestSubject()
        v = t.combine_strings("This", "is", "a", "test")
        self.assertEqual(v, "THIS IS A TEST", "Test case failed for combine_strings()!")


if __name__ == "__main__":
    unittest.main()
