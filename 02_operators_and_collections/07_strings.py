# Common String Methods & Formatting

text = "  python programming 101  "

# Trimming whitespace
clean_text = text.strip()
print(f"Original: '{text}'")
print(f"Stripped: '{clean_text}'")

# Case transformations
print("\nupper():", clean_text.upper())
print("title():", clean_text.title())
print("capitalize():", clean_text.capitalize())

# Substring operations
print("\n'python' in string:", "python" in clean_text)
print("Count of 'o':", clean_text.count("o"))
