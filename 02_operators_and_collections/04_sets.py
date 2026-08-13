# Sets & Removing Duplicates

# Sets are unordered collections of unique elements.

# 1. Creating sets
numbers_set = {1, 2, 3, 3, 4}
print("Set auto-removes duplicates:", numbers_set)

# 2. Removing duplicates from a list using set()
employees = ["Kevin", "Gem", "Anja", "John", "Anja"]
unique_employees = list(set(employees))

print("\nOriginal list:", employees)
print("Unique list:", unique_employees)
print("Duplicates removed:", len(employees) - len(unique_employees))
