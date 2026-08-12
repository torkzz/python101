# # # # # # # # # # # # import re

# # # # # # # # # # # # # Common regex symbol
# # # # # # # # # # # # # \d -- digit
# # # # # # # # # # # # # \w -- word character
# # # # # # # # # # # # # \s -- whitespace
# # # # # # # # # # # # # .  -- any character
# # # # # # # # # # # # # +  -- one or more
# # # # # # # # # # # # # *  -- zero or more
# # # # # # # # # # # # # ?  -- optional
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # text = "My contact number is 0917-123-4567"



# # # # # # # # # # # # # result= re.findall(r"\d", text)
# # # # # # # # # # # # # print (result)
# # # # # # # # # # # # # print (type(result))



# # # # # # # # # # # # # result= re.findall(r"\d+", text)
# # # # # # # # # # # # # print (result)
# # # # # # # # # # # # # print (type(result))



# # # # # # # # # # # # text = """
# # # # # # # # # # # # Name: Kevin Paul
# # # # # # # # # # # # Contact: 0917-123-4567
# # # # # # # # # # # # Email: kevin@gmail.com
# # # # # # # # # # # # Age: 25
# # # # # # # # # # # # Student ID: 2025-001
# # # # # # # # # # # # """

# # # # # # # # # # # # # digits = re.findall(r"\d+", text)
# # # # # # # # # # # # # print(digits)


# # # # # # # # # # # # # phone_pattern = r"\d{4}-\d{3}-\d{4}"
# # # # # # # # # # # # # phones = re.findall(phone_pattern, text)
# # # # # # # # # # # # # print(phones)


# # # # # # # # # # # # # email_pattern = r"\S+@\S*"
# # # # # # # # # # # # # emails = re.findall(email_pattern, text)
# # # # # # # # # # # # # print(emails)


# # # # # # # # # # # # # result = re.search(r"\d+", text)
# # # # # # # # # # # # # result = re.search(r"\d+", text)

# # # # # # # # # # # # # print("Object:", result)
# # # # # # # # # # # # # print("Type:", type(result))
# # # # # # # # # # # # # print("Match:", result.group())
# # # # # # # # # # # # # print("Start:", result.start())
# # # # # # # # # # # # # print("End:", result.end())
# # # # # # # # # # # # # print("Span:", result.span())
# # # # # # # # # # # # # print(dir(result))
# # # # # # # # # # # # # # help(result)



# # # # # # # # # # # # # print(phone_number)
# # # # # # # # # # # # # \s+ characters before @
# # # # # # # # # # # # # email_pattern = r"\S+@\S+"

# # # # # # # # # # # # # emails = re.findall(email_pattern, text)
# # # # # # # # # # # # # print(emails)

# # # # # # # # # # # # # result = re.search(r"\d+", text)
# # # # # # # # # # # # # print(result.group())

# # # # # # # # # # # # # #fullmatch()

# # # # # # # # # # # # # result1 = re.fullmatch(r"\d+", text)
# # # # # # # # # # # # # print(result1)

# # # # # # # # # # # # sample = "Python123"

# # # # # # # # # # # # print(re.match(r"Python", sample))
# # # # # # # # # # # # print(re.search(r"123", sample))
# # # # # # # # # # # # print(re.findall(r"\d", sample))
# # # # # # # # # # # # print(re.findall(r"\w+", sample))



# # # # # # # # # # # # print("English :", "Hello")
# # # # # # # # # # # # print("Japanese:", "こんにちは")
# # # # # # # # # # # # print("Korean  :", "안녕하세요")
# # # # # # # # # # # # print("Chinese :", "你好")
# # # # # # # # # # # # print("Arabic  :", "مرحبا")

# # # # # # # # # # # # print()

# # # # # # # # # # # # print()

# # # # # # # # # # # # print("Fire Rocket Snake:")
# # # # # # # # # # # # print("🔥 🚀 🐍")

# # # # # # # # # # # # print("\u03A4")  # Τ → uppercase Tau
# # # # # # # # # # # # print("\u0393")  # Γ → uppercase Gamma
# # # # # # # # # # # # print("\u03A6")  # Φ → uppercase Phi

# # # # # # # # # # # # text = "Python 🔥"
# # # # # # # # # # # # encoded_text = text.encode('utf-8')

# # # # # # # # # # # # print(encoded_text)



# # # # # # # # # # # # # text2 = b"Python \xf0\x9f\x94\xa5"
# # # # # # # # # # # # # decode_text = text2.decode("utf-8")
# # # # # # # # # # # # # print(decode_text)




# # # # # # # # # # # # # print(ord('A'))
# # # # # # # # # # # # # print(chr(65))


# # # # # # # # # # # # # ord("👨‍👩‍👧‍👦")

# # # # # # # # # # # # # for number in range(1, 55295):
# # # # # # # # # # # # #     print(number, chr(number))
# # # # # # # # # # # # # print('こんにちは'.encode('ascii'))

# # # # # # # # # # # # # print('こんにちは'.encode('utf-8'))



# # # # # # # # # # # # with open('unicode_demo.txt', 'w', encoding='utf-8') as file:
# # # # # # # # # # # #     file.write('Hello python and hello 🌎')

# # # # # # # # # # # # print("File written successfully.")

# # # # # # # # # # # # with open('unicode_demo2.txt', 'w') as file:
# # # # # # # # # # # #     file.write('Hello python and hello 🌎')

# # # # # # # # # # # # print("File written successfully.")
# # # # # # # # # # # # with open('unicode_demo2.txt', 'a') as file:
# # # # # # # # # # # #     file.write('Hello python and hello 🌎')

# # # # # # # # # # # # import json

# # # # # # # # # # # # student = {
# # # # # # # # # # # #     'name': 'Kevin',
# # # # # # # # # # # #     'message': 'こんにちは',
# # # # # # # # # # # #     'emoji': '🔥 🐍'
# # # # # # # # # # # # }

# # # # # # # # # # # # # json.dumps() - Python object → JSON string
# # # # # # # # # # # # json_data = json.dumps(student, ensure_ascii=False)

# # # # # # # # # # # # print(json_data)

# # # # # # # # # # # # # json.loads() - JSON string → Python object
# # # # # # # # # # # # student_data = json.loads(json_data)

# # # # # # # # # # # # print(student_data)
# # # # # # # # # # # # print(student_data['name'])
# # # # # # # # # # # # print(student_data['message'])
# # # # # # # # # # # # print(student_data['emoji'])
# # # # # # # # # # # import json

# # # # # # # # # # # # student = {
# # # # # # # # # # # #     'name': 'Kevin',
# # # # # # # # # # # #     'message': 'こんにちは',
# # # # # # # # # # # #     'emoji': '🔥 🐍'
# # # # # # # # # # # # }

# # # # # # # # # # # # # json.dumps() → Python object to JSON string
# # # # # # # # # # # # json_data = json.dumps(student, ensure_ascii=False)

# # # # # # # # # # # # print(json_data)

# # # # # # # # # # # # # json.dump() → Python object directly to JSON file
# # # # # # # # # # # # with open('student.json', 'w', encoding='utf-8') as file:
# # # # # # # # # # # #     json.dump(student, file, ensure_ascii=False, indent=4)

# # # # # # # # # # # # print("JSON file created successfully.")


# # # # # # # # # # # # with open(
# # # # # # # # # # # #     'example.txt',
# # # # # # # # # # # #     'r',
# # # # # # # # # # # #     encoding='utf-8'
# # # # # # # # # # # # ) as file:

# # # # # # # # # # # #     for line_number, line in enumerate(file, start=1):

# # # # # # # # # # # #         print(
# # # # # # # # # # # #             f"{line_number}: {line.strip()}"
# # # # # # # # # # # #         )

# # # # # # # # # # # # print()


# # # # # # # # # # # with open(
# # # # # # # # # # #     'example.txt',
# # # # # # # # # # #     'r',
# # # # # # # # # # #     encoding='utf-8'
# # # # # # # # # # # ) as file:
# # # # # # # # # # #     print(type(file))

# # # # # # # # # # #     for line_number, line in enumerate(file, start=1):

# # # # # # # # # # #         print(
# # # # # # # # # # #             f"{line_number}: {line.strip()}"
# # # # # # # # # # #         )

# # # # # # # # # # # print()




# # # # # # # # # # # Exceptions
# # # # # # # # # # #
# # # # # # # # # # # The following are the common types of Python exceptions.
# # # # # # # # # # #
# # # # # # # # # # # Exception            When It Occurs
# # # # # # # # # # #
# # # # # # # # # # # SyntaxError          Python cannot parse your code due to invalid syntax
# # # # # # # # # # #
# # # # # # # # # # # IndentationError     Subtype of SyntaxError; invalid indentation
# # # # # # # # # # #
# # # # # # # # # # # AttributeError       Accessing a nonexistent attribute/method
# # # # # # # # # # #
# # # # # # # # # # # NameError             Using an undefined variable
# # # # # # # # # # #
# # # # # # # # # # # IndexError            Accessing invalid index in a sequence
# # # # # # # # # # #
# # # # # # # # # # # TypeError             Wrong type for operation or function
# # # # # # # # # # #
# # # # # # # # # # # ValueError            Correct type but inappropriate value
# # # # # # # # # # #
# # # # # # # # # # # ZeroDivisionError     Division or modulo by zero
# # # # # # # # # # #
# # # # # # # # # # # FileNotFoundError     File does not exist


# # # # # # # # # # # Wildcard except clauses
# # # # # # # # # # #
# # # # # # # # # # # Catch any exception without specifying the type.

# # # # # # # # # # # Simple program that demonstrates without handling
# # # # # # # # # # print("hello world")

# # # # # # # # # # # Output:
# # # # # # # # # # # SyntaxError: invalid syntax.
# # # # # # # # # # # Perhaps you forgot a comma?

# # # # # # # # # # try:
# # # # # # # # # #     print("hello world")
# # # # # # # # # # except:  # Wildcard clause
# # # # # # # # # #     print("Something went wrong: Invalid syntax!")

# # # # # # # # # # # Output:
# # # # # # # # # # # Something went wrong: Invalid syntax!

# # # # # # # # # # Getting Information on Exceptions
# # # # # # # # # #
# # # # # # # # # # When an exception occurs, it often carries details about the error:
# # # # # # # # # # the type of exception, e.g., SyntaxError, ZeroDivisionError.
# # # # # # # # # #
# # # # # # # # # # The following are some examples:


# # # # # # # # # # ValueError

# # # # # # # # # try:
# # # # # # # # #     x = int("abc")  # causes ValueError
# # # # # # # # # except ValueError as e:
# # # # # # # # #     print("Error:", e)

# # # # # # # # # # Output:
# # # # # # # # # # Error: invalid literal for int() with base 10: 'abc'


# # # # # # # # # # ZeroDivisionError

# # # # # # # # # try:
# # # # # # # # #     result = 10 / 0  # causes ZeroDivisionError
# # # # # # # # # except ZeroDivisionError as e:
# # # # # # # # #     print("Error:", e)

# # # # # # # # # # Output:
# # # # # # # # # # Error: division by zero

# # # # # # # # # Getting Information on Exceptions
# # # # # # # # #
# # # # # # # # # When an exception occurs, it often carries details about the error:
# # # # # # # # # the type of exception, e.g., SyntaxError, ZeroDivisionError.
# # # # # # # # #
# # # # # # # # # The following are some examples:


# # # # # # # # # ValueError

# # # # # # # # try:
# # # # # # # #     x = int("abc")  # causes ValueError
# # # # # # # # except ValueError as e:
# # # # # # # #     print("Error:", e)

# # # # # # # # # Output:
# # # # # # # # # Error: invalid literal for int() with base 10: 'abc'


# # # # # # # # # ZeroDivisionError

# # # # # # # # try:
# # # # # # # #     result = 10 / 0  # causes ZeroDivisionError
# # # # # # # # except ZeroDivisionError as e:
# # # # # # # #     print("Error:", e)

# # # # # # # # # Output:
# # # # # # # # # Error: division by zero


# # # # # # # # # The else Clause
# # # # # # # # #
# # # # # # # # # The else clause runs only if no exception occurs in the try block.

# # # # # # # # try:
# # # # # # # #     num = int(input("Enter a number: "))
# # # # # # # #     result = 10 / num

# # # # # # # # except ValueError as v:
# # # # # # # #     print(v)

# # # # # # # # except ZeroDivisionError as e:
# # # # # # # #     print(e)

# # # # # # # # else:
# # # # # # # #     print("Success! Result is", result, ".")

# # # # # # # #     # The finally Clause
# # # # # # # # #
# # # # # # # # # The finally clause always runs, no matter what happens
# # # # # # # # # in the try or except blocks.
# # # # # # # # #
# # # # # # # # # It is used for cleanup tasks, such as closing files,
# # # # # # # # # releasing resources, or ending connections.


# # # # # # # # try:
# # # # # # # #     f = open("data.txt", "r")
# # # # # # # #     content = f.read()
# # # # # # # #     print(content)

# # # # # # # # except FileNotFoundError as fe:
# # # # # # # #     print(fe)

# # # # # # # # finally:
# # # # # # # #     if 'f' in locals():
# # # # # # # #         f.close()  # Always closes the file


# # # # # # # # Using Exceptions for Flow Control
# # # # # # # #
# # # # # # # # Sometimes you can use exceptions to manage the flow of your program,
# # # # # # # # especially in cases where an operation may fail.

# # # # # # # while True:
# # # # # # #     try:
# # # # # # #         user_input = input("Enter a positive integer: ")
# # # # # # #         n = int(user_input)  # Might raise ValueError

# # # # # # #         if n > 0:
# # # # # # #             break  # Exit loop if input is valid

# # # # # # #     except ValueError:
# # # # # # #         print(f'"{user_input}" cannot be converted to an int!')

# # # # # # # print(f'You have entered {n}, a positive integer.')



# # # # # # # Raising your Own Exception
# # # # # # #
# # # # # # # You can manually raise an exception using the raise keyword.
# # # # # # #
# # # # # # # Syntax:
# # # # # # # raise ExceptionType("Error message")
# # # # # # #
# # # # # # # raise: signal errors manually.
# # # # # # # ExceptionType: can be built-in (like ValueError)
# # # # # # #                or a custom exception class.
# # # # # # # "Error message": a description of what went wrong.


# # # # # # def check_age(age):
# # # # # #     if age < 0:
# # # # # #         raise ValueError("Age cannot be negative!")

# # # # # #     return f"Age is {age}"


# # # # # # print(check_age(25))   # Age is 25
# # # # # # print(check_age(-5))   # Raises ValueError

# # # # # # Exception Hierarchy
# # # # # #
# # # # # # Python organizes exceptions in a hierarchical tree,
# # # # # # where some exceptions are subclasses of others.
# # # # # #
# # # # # # The base class for all exceptions is BaseException.


# # # # # # Simplified hierarchy:
# # # # # #
# # # # # # BaseException
# # # # # # └── Exception
# # # # # #     ├── ArithmeticError
# # # # # #     │   ├── FloatingPointError
# # # # # #     │   ├── OverflowError
# # # # # #     │   └── ZeroDivisionError
# # # # # #     │
# # # # # #     ├── AttributeError
# # # # # #     ├── BufferError
# # # # # #     ├── EOFError
# # # # # #     ├── ImportError
# # # # # #     │   └── ModuleNotFoundError
# # # # # #     │
# # # # # #     ├── LookupError
# # # # # #     │   ├── IndexError
# # # # # #     │   └── KeyError
# # # # # #     │
# # # # # #     ├── MemoryError
# # # # # #     ├── NameError
# # # # # #     ├── OSError
# # # # # #     │   ├── FileNotFoundError
# # # # # #     │   ├── PermissionError
# # # # # #     │   └── TimeoutError
# # # # # #     │
# # # # # #     ├── RuntimeError
# # # # # #     │   ├── NotImplementedError
# # # # # #     │   └── RecursionError
# # # # # #     │
# # # # # #     ├── SyntaxError
# # # # # #     ├── SystemError
# # # # # #     ├── TypeError
# # # # # #     └── ValueError
# # # # # #
# # # # # #
# # # # # # Important:
# # # # # # More specific exceptions should generally be caught first,
# # # # # # followed by more general exceptions.

# # # # # try:
# # # # #     value = int("abc")

# # # # # except ValueError:
# # # # #     print("ValueError occurred")

# # # # # except Exception:
# # # # #     print("Some other exception occurred")


# # # # # Exception Hierarchy

# # # # try:
# # # #     lst = [1, 2, 3]
# # # #     print(lst[5])

# # # # except ValueError:
# # # #     print("Caught ValueError")

# # # # except KeyError:
# # # #     print("Caught KeyError")

# # # # except IndexError:
# # # #     print("Caught IndexError")

# # # # except Exception:
# # # #     print("Caught general exception")
# # # #
# # # #
# # # import time

# # # current_timestamp = time.time()

# # # print(current_timestamp)

# # # print(time.ctime(current_timestamp))

# # # print(time.localtime(current_timestamp))


# # import time

# # current_timestamp = time.time()

# # print(current_timestamp)

# # current_time = time.ctime()
# # print(current_time)

# # local = time.localtime()

# # print(local.tm_yday)


# import time

# current_timestamp = time.time()

# print(current_timestamp)

# current_time = time.ctime()
# print(current_time)

# local = time.localtime()
# print(local.tm_hour)


# log_time = time.localtime()

# log_message = (
#     f"{log_time.tm_year}-"
#     f"{log_time.tm_mon:02d}-"
#     f"{log_time.tm_mday:02d} "
#     f"{log_time.tm_hour:02d}:"
#     f"{log_time.tm_min:02d}:"
#     f"{log_time.tm_sec:02d} "
#     f"Server started successfully."
# )

# print(log_message)

# print()


# countdown timer
import time

for number in range(5, 0, -1):

    print(f"Shutting down in {number}...")

    time.sleep(2)

print()

print("System process started!")