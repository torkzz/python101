# Variables, Data Types & Comparisons

# 1. Basic Data Types
name = "John"           # str
age = 25                # int
gpa = 3.8               # float
is_student = True       # bool

print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"GPA: {gpa} ({type(gpa).__name__})")

# 2. Floating-point Division & Rounding
pi_approx = 22 / 7
print("\n22 / 7 =", pi_approx)
print("Rounded to 2 decimals:", round(pi_approx, 2))

# 3. Comparison & Logical Operators
x, y = 10, 20
print("\nx < y:", x < y)
print("x == y:", x == y)
print("Logical AND:", (x < y) and (y > 15))
print("Logical NOT:", not (x == y))
