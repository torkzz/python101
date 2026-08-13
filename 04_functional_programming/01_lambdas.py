# Lambda Functions & Functional Features

# 1. Lambda syntax: lambda arguments: expression
exponent = lambda base, exp=2: base ** exp

print("4 squared (default exp=2):", exponent(4))
print("4 cubed:", exponent(4, 3))

# 2. Inline conditional logic inside lambda
is_even = lambda n: "Even" if n % 2 == 0 else "Odd"

print("\n10 is:", is_even(10))
print("7 is:", is_even(7))

# 3. Use lambda with map() and filter()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x ** 2, numbers))

print("\nEvens (filter):", evens)
print("Squares (map):", squares)
