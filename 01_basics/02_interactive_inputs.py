# Interactive Terminal Calculator & Type Checker

def run_calculator():
    print("=== Interactive Calculator & Type Inspector ===")
    
    val1_raw = input("Enter first value: ").strip()
    val2_raw = input("Enter second value: ").strip()

    # Dynamic type inference demo
    def infer_type(val):
        if val.isdigit():
            return int(val)
        try:
            return float(val)
        except ValueError:
            return val

    val1 = infer_type(val1_raw)
    val2 = infer_type(val2_raw)

    print(f"\nValue 1: {val1!r} | Inferred Type: {type(val1).__name__}")
    print(f"Value 2: {val2!r} | Inferred Type: {type(val2).__name__}")

    # Operations if both are numeric
    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        print(f"\nAddition ({val1} + {val2}):", val1 + val2)
        print(f"Subtraction ({val1} - {val2}):", val1 - val2)
        print(f"Multiplication ({val1} * {val2}):", val1 * val2)
        if val2 != 0:
            print(f"Division ({val1} / {val2}):", val1 / val2)
            print(f"Floor Division ({val1} // {val2}):", val1 // val2)
            print(f"Modulo ({val1} % {val2}):", val1 % val2)
        else:
            print("Division by zero skipped!")
    else:
        print("\nConcatenation (String mode):", str(val1) + str(val2))

if __name__ == "__main__":
    run_calculator()
