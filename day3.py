# Control Flow, Generators & List Comprehensions

# 1. Enumerate: loop with index
items = ["Mouse", "Keyboard", "Monitor"]
print("Enumerate output:")
for index, item in enumerate(items, start=1):
    print(f"  {index}. {item}")

# 2. Generator: yield values one at a time (memory efficient)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("\nGenerator output:", list(countdown(3)))

# 3. List Comprehension: [expression for item in iterable if condition]
employees = [
    {"name": "John", "salary": 25000},
    {"name": "Bea", "salary": 32000},
    {"name": "Cath", "salary": 15000},
]

high_earners = [e["name"] for e in employees if e["salary"] >= 20000]
print("\nHigh earners (List Comp):", high_earners)
