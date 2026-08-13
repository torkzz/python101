"""
Packing & Unpacking Arguments: *args and **kwargs

Concept -> Syntax -> Output -> Explanation -> Practical Exercises
"""

# 1. Packed Positional Arguments (*args -> tuple)
def packed_single_args(*args):
    print(type(args))
    print("Packed args:", args)

# 2. Packed Keyword Arguments (**kwargs -> dict)
def packed_kv_args(**kwargs):
    print(type(kwargs))
    print("Packed KV args:", kwargs)

# 3. Combined Fixed Parameter, *args, and **kwargs
def combined_packed_args(number: int, *args, **kwargs):
    print("Combined packed args:\n{}\n{}".format(args, kwargs))
    print("Number: ", number)

print("--- 1. Single Packed Positional Arguments (*args) ---")
packed_single_args("Apple", "Banana", "Cherry", "Durian")

print("\n--- 2. Single Packed Keyword Arguments (**kwargs) ---")
packed_kv_args(name="Mark", age=30, job_role="IT Trainer")

print("\n--- 3. Combined Fixed Parameter + *args + **kwargs ---")
combined_packed_args(
    1,
    "Apple",
    "Banana",
    "Cherry",
    favorite_fruit="Apple",
    least_favorite_fruit="Durian"
)

# 4. Packing vs Unpacking
"""
Packing (Function Definition):
  def func(*args, **kwargs) -> Packs arguments into tuple & dict.

Unpacking (Function Call):
  func(*list_val, **dict_val) -> Unpacks items into separate arguments.
"""
print("\n--- 4. Unpacking Collections in Function Calls ---")
fruits = ["Apple", "Banana", "Cherry"]
user_info = {"name": "Kevin", "age": 30}

# Unpacking list into *args
packed_single_args(*fruits)

# Unpacking dict into **kwargs
packed_kv_args(**user_info)

# 5. Practical Exercises & Solutions

# Exercise 1: Sum all numbers passed via *args
def sum_all(*args: float) -> float:
    return sum(args)

# Exercise 2: Find max value from *args
def find_max(*args: float) -> float:
    return max(args) if args else 0.0

# Exercise 3 & 4: Print employee kwargs with a loop
def print_employee_info(**kwargs) -> None:
    for key, value in kwargs.items():
        print(f"  {key.title()}: {value}")

print("\n--- 5. Practical Exercises Output ---")
print("Sum (10, 20, 30):", sum_all(10, 20, 30))
print("Max (5, 99, 12):", find_max(5, 99, 12))
print("Employee Info:")
print_employee_info(name="Kevin", role="DevOps", score=95)
