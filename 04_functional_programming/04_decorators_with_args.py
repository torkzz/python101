"""
Decorators with Function Arguments

Concepts:
- Decorators accepting target function and wrapping execution with arguments.
- Decorator execution timing: Runs at function definition time (printing function reference).
- Wrapper function (`multiply_values`) intercepting arguments `(x, y)`.
- Overriding passed arguments inside wrapper before calling decorated `func(10, 5)`.
"""

from typing import Callable


def two_values(func: Callable[[int, int], None]) -> Callable[[int, int], None]:
    # Prints original function reference when @two_values is applied
    print("Original target function:", func)

    def multiply_values(x: int, y: int) -> None:
        print("Multiplied values:", x * y)
        # Executes wrapped function with hardcoded values 10, 5
        return func(10, 5)

    # Prints wrapper function reference returned by decorator
    print("Wrapper function reference:", multiply_values)
    return multiply_values


# @two_values wraps add_values at definition time
@two_values
def add_values(x: int, y: int) -> None:
    print("Added values:", x + y)


def main() -> None:
    print("\n--- Calling Decorated add_values(4, 6) ---")
    # Calling add_values actually executes multiply_values(4, 6)
    add_values(4, 6)


if __name__ == "__main__":
    main()
