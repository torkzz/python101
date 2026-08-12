# True
# False
# Logical operators
# not, and, or

# and -- 2 statement are true the truth values is true;otherwise false
# print("\nAND Operator")
# print(True and True)
# print(True and False)

# # or -- as long as one of the statement is true the truth values is trul otherwise false
# print("\nOR Operator")
# print(True or False)
# print(False or False)

# # not
# print("\nNOT Operator")
# print(not True)
# print(not False)
# print(True and not False)
# print( not not not True)



# Loop Counter
# attempts = 0
# max_attempts = 3

# correct_username = "admin"
# correct_password = "1234"

# while attempts < max_attempts:
#     print(f"\nAttempt #{attempts + 1}")

#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == correct_username and password == correct_password:
#         print("\nAccess Granted")
#         print(f"Welcome, {username.title()}")
#         break  # it stops the loop immediately

#     else:
#         print("\nInvalid username or password")

#     attempts += 1

#     remaining = max_attempts - attempts

#     print(f"Remaining attempts: {remaining}")

# else:
#     print("\nToo many failed attempts")
#     print("Account temporarily locked")

# print("\nSystem Ended")
# enumerate() (start=1)

# items = [
#     "Mouse",
#     "Keyboard",
#     "Monitor",
#     "Webcam",
#     "Headset"
# ]

# for index, item in enumerate(items, 1):
#     print(f"{index}. {item}")


# A generator is a special type
# of function that produces values
# ONE AT A TIME
# using the yield keyword.

# def countdown(start):
#     print("Starting countdown...\n")

#     while start > 0:
#         yield start
#         start -= 1


# for number in countdown(5):
#     print(number)



# [expression for item in sequence]

# scores = [75, 80, 95, 60, 88, 72, 99]

# passed = [score for score in scores if score >= 75]

# print(passed)

# c = [x ** x for x in (1, 2, 3)]

# print(c)
# print(type(c))


employees = [
    {"name": "John", "salary": 25000},
    {"name": "Bea", "salary": 32000},
    {"name": "Cath", "salary": 15000},
    {"name": "Danica", "salary": 28000}
]

# for employee in employees:
#     print(employee)

high_salary = [
    employee["name"]
    for employee in employees
    if employee["salary"] >= 20000
]

print(high_salary)


employees = [
    {"name": "John", "salary": 25000},
    {"name": "Bea", "salary": 32000},
    {"name": "Cath", "salary": 15000},
    {"name": "Danica", "salary": 28000}
]

# for employee in employees:
#     print(employee)

high_salary = [f"{employee['name']}: {employee['salary']}" for employee in employees if employee["salary"] >= 20000]

print(high_salary)
