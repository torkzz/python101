"""
Packing & Unpacking Arguments: *args and **kwargs

Core Concepts:
- *args   : Packs variable positional arguments into an IMMUTABLE TUPLE.
- **kwargs: Packs variable keyword (key=value) arguments into a MUTABLE DICTIONARY.
- Order in parameters: Standard params -> *args -> **kwargs.
- Unpacking (* / **): Spreads elements from iterables/dicts into individual arguments.
"""

# 1. Packed Positional Arguments (*args)
# The asterisk (*) tells Python to gather extra non-keyword arguments into a tuple.
def packed_single_args(*args):
    # Output <class 'tuple'> because args is stored as a tuple
    print("Type:", type(args))
    # Output ('Apple', 'Banana', 'Cherry', 'Durian')
    print("Packed args:", args)


# 2. Packed Keyword Arguments (**kwargs)
# Double asterisks (**) gather extra named key=value arguments into a dictionary.
def packed_kv_args(**kwargs):
    # Output <class 'dict'> because kwargs is stored as a dictionary
    print("Type:", type(kwargs))
    # Output {'name': 'Mark', 'age': 30, 'job_role': 'IT Trainer'}
    print("Packed KV args:", kwargs)


# 3. Combined Fixed Parameter, *args, and **kwargs
# Parameter order rule: 1) Fixed positionals, 2) *args, 3) **kwargs
def combined_packed_args(number: int, *args, **kwargs):
    # number gets 1
    # args gets ('Apple', 'Banana', 'Cherry')
    # kwargs gets {'favorite_fruit': 'Apple', 'least_favorite_fruit': 'Durian'}
    print("Combined packed args:\n{}\n{}".format(args, kwargs))
    print("Number: ", number)


# 4. Explicit Unpacking into Fixed Function Parameters
# Unpacking iterable elements into fixed positional arguments (x, y, z, a)
def unpacked_single_args(x: str, y: str, z: str, a: str):
    print("Unpacked values:", x, y, z, a)


# Unpacking dictionary key-values into matching named parameters (age, course, name)
def unpacked_kv_args(age: int, course: str, name: str):
    print("Unpacked KV args:", name, age, course)


print("--- 1. Single Packed Positional Arguments (*args) ---")
# 'Apple', 'Banana', 'Cherry', 'Durian' passed as 4 separate arguments -> packed into tuple
packed_single_args("Apple", "Banana", "Cherry", "Durian")

print("\n--- 2. Single Packed Keyword Arguments (**kwargs) ---")
# Key=value pairs passed -> packed into dictionary
packed_kv_args(name="Mark", age=30, job_role="IT Trainer")

print("\n--- 3. Combined Fixed Parameter + *args + **kwargs ---")
# 1 -> number (int)
# "Apple", "Banana", "Cherry" -> *args (tuple)
# favorite_fruit=..., least_favorite_fruit=... -> **kwargs (dict)
combined_packed_args(
    1,
    "Apple",
    "Banana",
    "Cherry",
    favorite_fruit="Apple",
    least_favorite_fruit="Durian"
)

print("\n--- 4. Unpacking Iterable & Dict into Explicit Parameters ---")
# Set of 4 items -> unpacked into positional arguments x, y, z, a
# Note: Sets are unordered, so exact assignment order depends on set iteration
fruits_set = {"Apple", "Banana", "Cherry", "Durian"}

student_data = {
    "name": "John",
    "age": 17,
    "course": "BSIT"
}

# *fruits_set spreads 4 items into x, y, z, a
unpacked_single_args(*fruits_set)

# **student_data spreads name, age, course into matching keyword arguments
unpacked_kv_args(**student_data)


# 5. Packing vs Unpacking Summary
"""
1. PACKING (Used in Function Definitions):
   def func(*args, **kwargs):
     gathers individual values into a tuple (*args) or dict (**kwargs).

2. UNPACKING (Used in Function Calls):
   func(*my_list, **my_dict):
     spreads a list/tuple/set into separate positional arguments,
     and spreads a dict into matching keyword arguments.
"""

# 6. Practical Exercises & Solutions

# Exercise 1: Sum all numbers passed via *args
def sum_all(*args: float) -> float:
    # args is a tuple of numbers, so built-in sum() works directly
    return sum(args)


# Exercise 2: Find max value from *args
def find_max(*args: float) -> float:
    # Return 0.0 if empty, otherwise max element in tuple
    return max(args) if args else 0.0


# Exercise 3 & 4: Print employee kwargs with a loop
def print_employee_info(**kwargs) -> None:
    # Iterate over dict items (key, value pairs)
    for key, value in kwargs.items():
        print(f"  {key.title()}: {value}")


print("\n--- 6. Practical Exercises Output ---")
print("Sum (10, 20, 30):", sum_all(10, 20, 30))
print("Max (5, 99, 12):", find_max(5, 99, 12))
print("Employee Info:")
print_employee_info(name="Kevin", role="DevOps", score=95)
