# Common String Methods & Slicing

text = "  python programming 101  "

# 1. Trimming whitespace
clean_text = text.strip()
print(f"Original: '{text}'")
print(f"Stripped: '{clean_text}'")

# 2. Case transformations
print("\nupper():", clean_text.upper())
print("title():", clean_text.title())
print("capitalize():", clean_text.capitalize())

# 3. String Slicing [start:stop:step]
sample = "Python"
print("\nSlice [0:4]:", sample[0:4])        # "Pyth"
print("Slice [::2]:", sample[::2])         # "Pto" (every 2nd char)
print("Reversed [::-1]:", sample[::-1])    # "nohtyP" (negative step reverses string)

# 4. Substring operations
print("\n'python' in string:", "python" in clean_text)
print("Count of 'o':", clean_text.count("o"))
