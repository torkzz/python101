"""
Python Documentation Standards (Docstrings) & Useful Language Tricks

Concepts:
- Docstrings (PEP 257 standard): Module, Class, and Function documentation.
- Built-in documentation inspection (`help()`, `dir()`, `__doc__`).
- Useful Python Tricks:
  1. Multiple Assignment & Swapping variables (`a, b = b, a`).
  2. Unpacking with wildcard `*rest`.
  3. F-string debug formatting (`f"{var=}"`).
  4. Dictionary merging (`{**dict1, **dict2}` and `|`).
  5. `zip()` for parallel iteration.
  6. Walrus operator `:=` (Assignment Expressions).
"""

from typing import Any


def calculate_discount(price: float, discount: float = 0.10) -> float:
    """Calculate the final price after applying a percentage discount.

    Args:
        price (float): Original price of the item.
        discount (float, optional): Discount percentage as float (0.10 = 10%). Defaults to 0.10.

    Returns:
        float: Final discounted price rounded to 2 decimal places.
    """
    return round(price * (1 - discount), 2)


def main() -> None:
    print("=== 1. Inspecting Docstrings & Help ===")
    print("Function docstring (__doc__):")
    print(calculate_discount.__doc__)

    print("\n=== 2. Useful Python Language Tricks ===")

    # Trick A: Variable Swapping (No temp variable needed)
    a, b = 5, 10
    a, b = b, a
    print(f"Swapped: {a=}, {b=}")

    # Trick B: Extended Unpacking (*rest)
    first, *middle, last = [10, 20, 30, 40, 50]
    print(f"Unpacked: {first=}, {middle=}, {last=}")

    # Trick C: F-String Self-Documenting Debug Expressions (var=)
    username = "dev_user"
    role = "admin"
    print(f"Debug Output: {username=}, {role=}")

    # Trick D: Parallel Iteration with zip()
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    print("\nZipped Iteration:")
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")

    # Trick E: Walrus Operator (:=) for inline assignment
    phrase = "Python Programming"
    if (n := len(phrase)) > 10:
        print(f"\nPhrase is long ({n} characters).")


if __name__ == "__main__":
    main()
