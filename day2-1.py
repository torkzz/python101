# Useful Built-in Functions

numbers = [5, 10, 15, 20]

# min() and max()
print("Min:", min(numbers))
print("Max:", max(numbers))

# divmod() returns (quotient, remainder) tuple
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5) -> Quotient: {quotient}, Remainder: {remainder}")

# all() returns True if ALL elements are truthy (non-zero/non-empty)
print("all([1, 2, 3]):", all([1, 2, 3]))
print("all([1, 0, 3]):", all([1, 0, 3]))

# any() returns True if AT LEAST ONE element is truthy
print("any([0, False, 5]):", any([0, False, 5]))
