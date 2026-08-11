# Operator Precedence
# create a simple operator precedence
#

# P -> Parentheses
# E -> Exponents
# M -> Multiplication
# D -> Division
# A -> Addition
# S -> Subtraction


# print("Example 1:")
# print("40 + 2 * 3")
# print("Answer:", 40 + 2 * 3)

# print()

# print("Example 2:")
# print("(40 + 2) * 3")
# print("Answer:", (40 + 2) * 3)

# print()

# print("Example 3:")
# print("3*2+4*8")
# print("Answer:", 3*2+4*8)

# print()

# print("Example 4:")
# print("3*(2+4)*8")
# print("Answer:", 3*(2+4)*8)


# print()
# print("Example 5:")
# print("50-20/5")
# print("Answer:", 50-20/5)

# print()
# print("Example 6:")
# print("50-20/5")
# print("Answer:", (50-20)/5)

# print()
# print("Example 7:")
# print("100/5*2-10")
# print("Answer:", 100/5*2-10)

# # print()
# # print("Example 7:")
# # print("100/(5*2-10)")
# # print("Answer:", 100/(5*2-10))

# print()
# print("Example 9:")
# print("10+4*2**3")
# print("Answer:", 10+4*2**3)

# print("Example 11:")
# print("18 / 3 ** 2")
# print("Answer:", 18 / 3 ** 2)

# print()

# print("Example 12:")
# print("2 ** 2 ** 3")
# print("Answer:", 2 ** 2 ** 3)

# print()

# Multiple exponents are evaluated
# from RIGHT to LEFT.

# COMMON OPERATOR PRECEDENCE
# Highest Priority
# ()
# **
# *, /,//-FLORDIV, %-MODULO
# +, -



# Floor Division and Modulo
# FD -- returns the quotient WITHOUT THE DECIMAL PART
# It rounds down to the nearest whole number
# negative, rounded down


# Modulo -- returns the remainder after division


# print("Example 1:")
# print("17 // 5 =", 17 // 5)
# print("17 % 5 =", 17 % 5)

# print()
# print("Example 2:")
# print(-17/5)
# print("-17 // 5 =", -17 // 5)
# print("-17 % 5 =", -17 % 5)

# print()
# print("Example 3:")
# print(-17/5)
# print("-17 // 5 =", 17 // -5)
# print("-17 % 5 =", 17 % -5)


# print()
# print("Example 4:")
# print(-17/5)
# print("-17 // 5 =", -17 // -5)
# print("-17 % 5 =", -17 % -5)

# print("Example 5:")
# print("0 // 5 =", 0 // 5)
# print("0 % 5 =", 0 % 5)

# print()
# Assignment Operator

total = 100

total += 25
print("Total 1: ", total)
print()

total *= 2
print("Total 2: ", total)
print()

total -= 50
print("Total 3: ", total)
print()

total //= 4
print("Total 4: ", total)
print()
total %= 6
print("Total 5: ", total)
print()

total **= 3
print("Total 6: ", total)
print()

total /= 2
print("Total 7: ", total)
print()
