# round(number, decimal_places)
print("3. round() Function")

print("round(3.14159, 2) =", round(3.14159, 2))

print()

# list
numbers = [5, 10, 15, 20]

print("Numbers:", numbers)

print()

# min()
print("4. min() Function")

print("Smallest number:", min(numbers))

print()




print("7. divmod() Function")

print("divmod(17, 5) =", divmod(17, 5))

print("Equivalent to:", (17 // 5, 17 % 5))

# all()
# Truthy values evaluate to true.
# non-zero numbers
# non-empty strings
# non-empty lists
#
print()

print("8. all() Function")

print("all([1, 2, 3]) =", all([1, 2, 3]))

print("all([1, -2, 3]) =", all([1, -2, 3]))

print("all([1, 0, 3]) =", all([1, 0, 3]))

print()


# Falsy Values
# 0
# 0.0
# empty strings "" or " "
# empty lists
# False
# None == null

# any()
# Returns True
# if AT LEAST ONE value
# is truthy.
