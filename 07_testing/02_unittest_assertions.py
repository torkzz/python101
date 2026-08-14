"""
Python unittest Assertion Methods Cheat Sheet & Usage Guide

Assertion Cheat Sheet:
| Assertion                   | Meaning                          |
| --------------------------- | -------------------------------- |
| assertEqual(a, b)           | a == b (value equality)          |
| assertNotEqual(a, b)        | a != b                           |
| assertTrue(x)               | x is True / truthy               |
| assertFalse(x)              | x is False / falsy               |
| assertIs(a, b)              | a is b (object identity)         |
| assertIsNot(a, b)           | a is not b                       |
| assertIsNone(x)             | x is None                        |
| assertIsNotNone(x)          | x is not None                    |
| assertIn(a, b)              | a in b                           |
| assertNotIn(a, b)           | a not in b                       |
| assertIsInstance(a, b)      | isinstance(a, b)                 |
| assertNotIsInstance(a, b)   | not isinstance(a, b)             |
| assertRaises(err)           | code should raise that exception |

Key Distinction:
- assertEqual(a, b): Checks VALUE EQUALITY ([1, 2] == [1, 2] -> True).
- assertIs(a, b)   : Checks OBJECT IDENTITY in memory (a is b).
"""

import unittest


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestAssertionsCheatSheet(unittest.TestCase):

    def test_equality_assertions(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(2, 3), 6)

    def test_boolean_assertions(self):
        self.assertTrue(add(2, 2) == 4)
        self.assertFalse(add(2, 2) == 5)

    def test_identity_assertions(self):
        a = None
        b = None
        # assertIs checks memory identity
        self.assertIs(a, b)
        self.assertIsNot(a, "not_none")

    def test_none_assertions(self):
        result = None
        val = 100
        self.assertIsNone(result)
        self.assertIsNotNone(val)

    def test_membership_assertions(self):
        fruits = ["Apple", "Banana", "Cherry"]
        self.assertIn("Apple", fruits)
        self.assertNotIn("Orange", fruits)

    def test_type_assertions(self):
        result = add(2, 3)
        self.assertIsInstance(result, int)
        self.assertNotIsInstance(result, str)

    def test_exception_assertions(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
