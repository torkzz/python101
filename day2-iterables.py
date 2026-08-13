# Iterables: Lists, Tuples, and Dictionaries

# 1. Lists (ordered, mutable)
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"             # Modify element
fruits.append("mango")           # Add item to end
print("List:", fruits)
print("Slice [1:3]:", fruits[1:3])

# 2. Tuples (ordered, immutable)
coords = (10.0, 20.0)
print("\nTuple:", coords)
print("X:", coords[0], "Y:", coords[1])

# 3. Dictionaries (key-value pairs, unique keys)
student = {"name": "Kevin", "age": 25, "course": "CS"}
print("\nDict get name:", student.get("name"))
print("Dict get fallback:", student.get("gpa", "N/A"))

# Convert key-value pairs list to dict
pairs = [("country", "Philippines"), ("currency", "Peso")]
info = dict(pairs)
print("Converted Dict:", info)
