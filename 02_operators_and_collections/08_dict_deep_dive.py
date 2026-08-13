# Dictionary Deep Dive: Methods, Views & Operations

# 1. Initialization patterns
user = {"id": 101, "username": "dev_user", "role": "admin"}
defaults = dict(status="active", retries=3)

# 2. Accessing & fallback values
print("Role:", user.get("role"))
print("Email (with fallback):", user.get("email", "not_set@example.com"))

# 3. Safe mutation & insertions
user.setdefault("login_count", 0)  # Sets key if missing, returns value
print("Login Count after setdefault:", user["login_count"])

# 4. Merging dictionaries (| operator in Python 3.9+)
merged_profile = user | defaults
print("\nMerged Profile (| operator):", merged_profile)

# 5. Dictionary views & iterations
print("\nKeys:", list(merged_profile.keys()))
print("Values:", list(merged_profile.values()))

print("\nIterating key-value pairs:")
for key, value in merged_profile.items():
    print(f"  {key}: {value}")

# 6. Dictionary Comprehension: {key_expr: value_expr for item in iterable}
scores = {"Alice": 85, "Bob": 62, "Charlie": 91}
passed_students = {k: v for k, v in scores.items() if v >= 75}
print("\nPassed Students (Dict Comp):", passed_students)
