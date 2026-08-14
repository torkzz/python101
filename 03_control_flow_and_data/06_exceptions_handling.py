"""
Exception Handling & Custom Errors (try / except / else / finally)

Concepts:
- Catching specific exceptions (`ValueError`, `ZeroDivisionError`).
- Exception clause `else`: Executes ONLY if NO exception was raised.
- Exception clause `finally`: ALWAYS executes (cleanup operations).
- Raising custom exceptions (`raise ValueError(...)`).
"""


def divide_numbers(a: float, b: float) -> float:
    """Safely divide numbers with custom zero division check."""
    if b == 0:
        raise ValueError("Custom Error: Cannot divide by zero!")
    return a / b


def run_exception_demo(val_str: str) -> None:
    print(f"\n--- Testing Input: '{val_str}' ---")
    try:
        num = float(val_str)
        result = divide_numbers(100.0, num)
    except ValueError as err:
        print(f"Caught ValueError: {err}")
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
    except Exception as err:
        print(f"Unexpected Exception: {err}")
    else:
        # Runs ONLY if try block succeeds without error
        print(f"Calculation Successful! Result: {result:.2f}")
    finally:
        # ALWAYS runs regardless of outcome
        print("Cleanup: Operation finished.")


if __name__ == "__main__":
    print("=== Exception Handling (try/except/else/finally) ===")
    run_exception_demo("20")       # Valid input
    run_exception_demo("0")        # Triggers division by zero error
    run_exception_demo("invalid")  # Triggers parsing error
