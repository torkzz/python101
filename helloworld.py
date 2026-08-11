# this is a comments
""" this is multi line
vic abalos from m360
doing for a living Software Engineer
matra Small improvements. Every day.
interest - i like playing gitar, tinkering stuff
reason - to have fundamentals on python
"""

# print("hello world")
# print(500)
# print(1,999,312) # 3 multiple values
# print(1999312)
# print(199.9312)


# print(10+2)
# print(10-2)
# print(10*2)
# print(10/2)
# print(2/10)
# print(20/4)
# print(20//4)

# X = "Anja"
# Y = 95
# Z = True

# print (X)
# print (Y)
# print (Z)


# test_var = 10
# test_var_2 = 20
# name = "John"
# ID_number = "IT010101"

# print(test_var)
# print(test_var_2)
# print(name)
# print(ID_number)



# print(type (test_var))
# print(type (test_var_2))
# print(type (name))
# print(type (ID_number))



# Float
# nearly_pi = 3.1415

# print(nearly_pi)
# print(type (nearly_pi))

# almost_py = 22/7
# print(almost_py)
# print(type (almost_py))

# print()
# print()

# almost_py = 22//7
# rouded_pi = round(almost_py, 5)
# print(almost_py)
# print(type (almost_py))
# print()
# print()
# print(rouded_pi)
# print(type (rouded_pi))

# rouded_pi = round(almost_py, 2)
# print(rouded_pi)
# print(type (rouded_pi))



# Strings
# my_number = "1.12321"
# print(my_number)
# print(type (my_number))
# print(len (my_number))
# print()
# print()

# also_my_number = float(my_number)
# print(also_my_number)
# print(type (also_my_number))


# new_string = "abc" +" "+ "def"
# print(new_string)
# print(type (new_string))
# print(len (new_string))


# new_string = "Martha "+ "Flor"
# print(new_string)
# print(type (new_string))
# print(len (new_string))


# new_string = "====####====" *5
# print(new_string)
# print(type(new_string))


# user_name = input("enter username")
# user_color= input("enter color")
# print(user_name)
# print(type(user_name))

# print(f" name  {user_name} color {user_color}")


# age = int(input("what is you age"))
# height = float(input("what is your height in cm"))


# print(f"your age is {age} and you height is {height}")


# a = int(input("ENter an integer:"))
# b = int(input("ENter another int :"))

# print ("Output:", a + b)


# help(print)
# help(len)


# student = ("kevin", 20, "BSIT")
# print(student)
# print(type(student))

# student = ["kevin", 20, "BSIT"]
# print(student)
# print(type(student))

# student = {"kevin", 20, "BSIT"}
# print(student)
# print(type(student))


# Module 1 Activity: Simple Mini Calculator

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# sum_result = round(num1 + num2, 2)
# diff_result = round(num1 - num2, 2)
# mult_result = round(num1 * num2, 2)

# print()

# print(f"SUM = {sum_result}")
# print(f"DIFFERENCE = {diff_result}")
# print(f"PRODUCT = {mult_result}")

# # Input
# item = input("Enter item: ")
# q = int(input("Enter quantity: "))
# p= float(input("Enter price per item: "))

# # Processing
# subtotal = q * p

# # Output
# print()
# print("="*10+"GROCERY RECEIPT"+"="*10)
# print(f"Item: {item}")
# print(f"Quantity: {q}")
# print(f"Price: ₱{p:.2f}")
# print(f"Subtotal: ₱{subtotal:.2f}")
# print("="*25)


# def myFunction():
#     print("I'm in a function!")
#     print("Still inside")

# myFunction()
# myFunction()
# myFunction()
# def Welcome(name):
#     print(f"Welcome to Python Fundamentals for Business Systems and Automation, {name}")


# Welcome("Kevin Paul")
# Welcome("Cath Ablag")
# Welcome("Danica Casino")
# Welcome("Francis Madrid")



# def Student(name, course):
#     print(f"Student {name} is enrolled in {course}")

# Student("Vic", "Python Fundamentals")


# def calculate_average(prelim, midterm, final):
#     average = (prelim + midterm + final) / 3
#     print(f"Average: {average:.2f}")


# calculate_average(91,100,79)
# def add(a, b):
#     return a + b

# result = add(5, 3)

# print(f"RESULT: {result}")

# def multiply_return(a, b):
#     return a * b


# result = multiply_return(2, 3)

# print(f"RESULT: {result}")


# def difference(a, b):
#     return a - b


# result = difference(10, 3)

# print(f"RESULT: {result}")



# def square(n):
#     return n * n

# result = square(5)

# print(f"RESULT: {result}")


# def greet(name):
#     return f"Hello, {name}"


# print(greet("Vic"))


# def divide(x, y):
#     return x / y

# c = divide(divide(12, 3), 2)

# print(f"Nested Function: {c}")


def is_passing(grade):
    return grade >= 75


result = is_passing(10)

print(f"Passing: {result}")



def square(number):
    return number * number
    print("This will not print")

result = square(5)
print(result)