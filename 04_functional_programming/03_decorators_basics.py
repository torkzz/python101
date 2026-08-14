"""
Python Decorators Basics

Concepts:
- Decorator Pattern: Functions as first-class objects (functions taking functions as arguments).
- Inner Wrapper Functions (`inner_method`).
- Decorator Syntax (`@decorator_method`).
- Modifying or extending function behavior without altering its source code.
"""

from typing import Callable


# 1. Defining a Decorator Function
# A decorator takes a target function (`func`) as an argument
def decorator_method(func: Callable[[], None]) -> Callable[[], None]:
    """Decorator that wraps a target function with additional print statements."""
    def inner_method() -> None:
        print("I am an inner decorator method")
        # Call original function
        func()

    # Return wrapper function reference
    return inner_method


# 2. Applying Decorator using @ Syntax
# @decorator_method is equivalent to: ordinary = decorator_method(ordinary)
@decorator_method
def ordinary() -> None:
    print("I am an ordinary method")


def main() -> None:
    print("=== Decorators Demo ===")
    # Calling ordinary() executes inner_method()
    ordinary()


if __name__ == "__main__":
    main()
