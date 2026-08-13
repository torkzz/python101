# Operator Precedence & Augmented Assignments

# 1. Operator Precedence (PEMDAS / BODMAS)
# Order: () -> ** -> *, /, //, % -> +, -
print("40 + 2 * 3 =", 40 + 2 * 3)       # 40 + 6 = 46
print("(40 + 2) * 3 =", (40 + 2) * 3)   # 42 * 3 = 126
print("2 ** 2 ** 3 =", 2 ** 2 ** 3)     # Exponents evaluate right-to-left: 2 ** 8 = 256

# 2. Floor Division (//) & Modulo (%)
# // returns quotient rounded down; % returns remainder.
print("\n17 // 5 =", 17 // 5)   # 3
print("17 % 5 =", 17 % 5)     # 2

# 3. Augmented Assignment Operators
total = 100
total += 25    # total = total + 25 -> 125
total *= 2     # total = total * 2  -> 250
total //= 4    # total = total // 4 -> 62
print("\nFinal total:", total)
