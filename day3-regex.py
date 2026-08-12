# import re

# # Common regex symbol
# # \d -- digit
# # \w -- word character
# # \s -- whitespace
# # .  -- any character
# # +  -- one or more
# # *  -- zero or more
# # ?  -- optional
# #
# #
# # text = "My contact number is 0917-123-4567"



# # result= re.findall(r"\d", text)
# # print (result)
# # print (type(result))



# # result= re.findall(r"\d+", text)
# # print (result)
# # print (type(result))



# text = """
# Name: Kevin Paul
# Contact: 0917-123-4567
# Email: kevin@gmail.com
# Age: 25
# Student ID: 2025-001
# """

# # digits = re.findall(r"\d+", text)
# # print(digits)


# # phone_pattern = r"\d{4}-\d{3}-\d{4}"
# # phones = re.findall(phone_pattern, text)
# # print(phones)


# # email_pattern = r"\S+@\S*"
# # emails = re.findall(email_pattern, text)
# # print(emails)


# # result = re.search(r"\d+", text)
# # result = re.search(r"\d+", text)

# # print("Object:", result)
# # print("Type:", type(result))
# # print("Match:", result.group())
# # print("Start:", result.start())
# # print("End:", result.end())
# # print("Span:", result.span())
# # print(dir(result))
# # # help(result)



# # print(phone_number)
# # \s+ characters before @
# # email_pattern = r"\S+@\S+"

# # emails = re.findall(email_pattern, text)
# # print(emails)

# # result = re.search(r"\d+", text)
# # print(result.group())

# # #fullmatch()

# # result1 = re.fullmatch(r"\d+", text)
# # print(result1)

# sample = "Python123"

# print(re.match(r"Python", sample))
# print(re.search(r"123", sample))
# print(re.findall(r"\d", sample))
# print(re.findall(r"\w+", sample))



# print("English :", "Hello")
# print("Japanese:", "こんにちは")
# print("Korean  :", "안녕하세요")
# print("Chinese :", "你好")
# print("Arabic  :", "مرحبا")

# print()

# print()

# print("Fire Rocket Snake:")
# print("🔥 🚀 🐍")

# print("\u03A4")  # Τ → uppercase Tau
# print("\u0393")  # Γ → uppercase Gamma
# print("\u03A6")  # Φ → uppercase Phi

# text = "Python 🔥"
# encoded_text = text.encode('utf-8')

# print(encoded_text)



# # text2 = b"Python \xf0\x9f\x94\xa5"
# # decode_text = text2.decode("utf-8")
# # print(decode_text)




# # print(ord('A'))
# # print(chr(65))


# # ord("👨‍👩‍👧‍👦")

# # for number in range(1, 55295):
# #     print(number, chr(number))
# # print('こんにちは'.encode('ascii'))

# # print('こんにちは'.encode('utf-8'))



# with open('unicode_demo.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello python and hello 🌎')

# print("File written successfully.")

# with open('unicode_demo2.txt', 'w') as file:
#     file.write('Hello python and hello 🌎')

# print("File written successfully.")
# with open('unicode_demo2.txt', 'a') as file:
#     file.write('Hello python and hello 🌎')

# import json

# student = {
#     'name': 'Kevin',
#     'message': 'こんにちは',
#     'emoji': '🔥 🐍'
# }

# # json.dumps() - Python object → JSON string
# json_data = json.dumps(student, ensure_ascii=False)

# print(json_data)

# # json.loads() - JSON string → Python object
# student_data = json.loads(json_data)

# print(student_data)
# print(student_data['name'])
# print(student_data['message'])
# print(student_data['emoji'])
import json

student = {
    'name': 'Kevin',
    'message': 'こんにちは',
    'emoji': '🔥 🐍'
}

# json.dumps() → Python object to JSON string
json_data = json.dumps(student, ensure_ascii=False)

print(json_data)

# json.dump() → Python object directly to JSON file
with open('student.json', 'w', encoding='utf-8') as file:
    json.dump(student, file, ensure_ascii=False, indent=4)

print("JSON file created successfully.")
