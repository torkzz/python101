

# # # # # # # # # # # # # # # # # lamba function
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # def exponent(base, exp):
# # # # # # # # # # # # # # # # #     return base ** exp

# # # # # # # # # # # # # # # # # exponent = lambda Float base, Float exp: base ** exp

# # # # # # # # # # # # # # # # # print('{}^{} = {}'.format(4, 6, exponent(4, 6)))


# # # # # # # # # # # # # # # # import random

# # # # # # # # # # # # # # # # # def exponent(base, exp):
# # # # # # # # # # # # # # # # #     return base ** exp

# # # # # # # # # # # # # # # # exponent = lambda base, exp = 2: base ** exp
# # # # # # # # # # # # # # # # # var = lambda [param1, param2, paramN...] : <code...>

# # # # # # # # # # # # # # # # rand = lambda: int(random.randrange(0, 100))

# # # # # # # # # # # # # # # # print('{}^{} = {}'.format(4, 2, exponent(4)))
# # # # # # # # # # # # # # # # print(rand())

# # # # # # # # # # # # # # # my_number = 37

# # # # # # # # # # # # # # # divisible_by_3 = lambda x: "Yes" if x % 3 == 0 else "No"
# # # # # # # # # # # # # # # print(divisible_by_3)
# # # # # # # # # # # # # # # # <expr_if_true> if <condition> else <expr_if_false>
# # # # # # # # # # # # # # my_number = 37

# # # # # # # # # # # # # # divisible_by_3 = lambda x: "Yes" if x % 3 == 0 else "No"
# # # # # # # # # # # # # # divisible_by_5_or_2 = lambda x: "Divisible by 5" if x % 5 == 0 else "Divisible by 2" if x % 2 == 0 else "Neither divisible by 5 or 2"
# # # # # # # # # # # # # # # <expr_if_true> if <condition> else <expr_if_false>

# # # # # # # # # # # # # # print("Is {} divisible by 3? {}".format(my_number, divisible_by_3(my_number)))
# # # # # # # # # # # # # # print("Is {} divisible by 3? {}".format(my_number, divisible_by_5_or_2(my_number)))
# # # # # # # # # # # # # names = [
# # # # # # # # # # # # #     {
# # # # # # # # # # # # #         "firstName": "Juan",
# # # # # # # # # # # # #         "lastName": "Dela Cruz"
# # # # # # # # # # # # #     },
# # # # # # # # # # # # #     {
# # # # # # # # # # # # #         "firstName": "Albert",
# # # # # # # # # # # # #         "lastName": "Santos"
# # # # # # # # # # # # #     },
# # # # # # # # # # # # #     {
# # # # # # # # # # # # #         "firstName": "Judy",
# # # # # # # # # # # # #         "lastName": "Agoncillo"
# # # # # # # # # # # # #     },
# # # # # # # # # # # # #     {
# # # # # # # # # # # # #         "firstName": "Joyce Ann",
# # # # # # # # # # # # #         "lastName": "Martinez"
# # # # # # # # # # # # #     },
# # # # # # # # # # # # #     {
# # # # # # # # # # # # #         "firstName": "Vic",
# # # # # # # # # # # # #         "lastName": "Abalos"
# # # # # # # # # # # # #     }
# # # # # # # # # # # # # ]

# # # # # # # # # # # # # sorted_names = sorted(names, key=lambda person: (person["lastName"],person["firstName"]))

# # # # # # # # # # # # # print(*sorted_names, sep='\n')
# # # # # # # # # # # # my_prices = [199.95, 109.99, 70.99, 49.99]

# # # # # # # # # # # # # def discounted_price(base_price):
# # # # # # # # # # # # #     return base_price - (base_price * .2)
# # # # # # # # # # # # #
# # # # # # # # # # # # discounted_price = lambda p: p - (p*.2 )

# # # # # # # # # # # # # print(list(map(discounted_price, my_prices)))
# # # # # # # # # # # # print(list(map(lambda p: p - (p*.2 ), my_prices)))


# # # # # # # # # # # # print(list(map(lambda p: str("{:.2f}".format(p - (p * .2))), my_prices)))

# # # # # # # # # # # # # final_prices = []

# # # # # # # # # # # # # for p in my_prices:
# # # # # # # # # # # # #     final_prices.append(discounted_price(p))

# # # # # # # # # # # # # print(final_prices)
# # # # # # # # # # # shapes = ["Rhombus", "Trapezoid", "Diamond", "Parallelogram", "Triangle"]

# # # # # # # # # # # print(list(map(lambda s: s + "shape", shapes)))


# # # # # # # # # # # fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Mango", "Apple"]

# # # # # # # # # # # print(fruits.count("Apple"))

# # # # # # # # # # # app_list = filter(lambda f: f.lower() =="apple", fruits)
# # # # # # # # # # # print(len(list(app_list)))
# # # # # # # # # # fruits_list = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Mango", "Apple"]
# # # # # # # # # # Today 10:45 AM
# # # # # # # # # # complete this
# # # # # # # # # # how about this ?



# # # # # # # # # # to text
# # # # # # # # # # Today 1:05 PM
# # # # # # # # # # to
# # # # # # # # # # make it tau gamma phi to text
# # # # # # # # # # here
# # # # # # # # # # Today 4:00 PM
# # # # # # # # # # to text



# # # # # # # # # # to text
# # # # # # # # # # to text
# # # # # # # # # # to text






# # # # # # # # # # i want shape to have something like shape sa dulo

# # # # # # # # # # Yes — your code is correct. 👍

# # # # # # # # # # shapes = ["Rhombus", "Trapezoid", "Diamond", "Parallelogram", "Triangle"]

# # # # # # # # # # # ...shape, e.g. Rhombusshape

# # # # # # # # # # print(list(map(lambda s: s + "shape", shapes)))

# # # # # # # # # # Output:

# # # # # # # # # # ['Rhombusshape', 'Trapezoidshape', 'Diamondshape', 'Parallelogramshape', 'Triangleshape']

# # # # # # # # # # If you want a space before "shape":

# # # # # # # # # # print(list(map(lambda s: s + " shape", shapes)))

# # # # # # # # # # Output:

# # # # # # # # # # ['Rhombus shape', 'Trapezoid shape', 'Diamond shape', 'Parallelogram shape', 'Triangle shape']
# # # # # # # # # # What your lambda is doing
# # # # # # # # # # lambda s: s + "shape"

# # # # # # # # # # For each item:

# # # # # # # # # # "Rhombus"       → "Rhombus" + "shape"       → "Rhombusshape"
# # # # # # # # # # "Trapezoid"     → "Trapezoid" + "shape"     → "Trapezoidshape"
# # # # # # # # # # "Diamond"       → "Diamond" + "shape"       → "Diamondshape"

# # # # # # # # # # And map() applies that lambda to every item in shapes.

# # # # # # # # # # shapes
# # # # # # # # # #   ↓
# # # # # # # # # # map(lambda...)
# # # # # # # # # #   ↓
# # # # # # # # # # modified items
# # # # # # # # # #   ↓
# # # # # # # # # # list()

# # # # # # # # # # So this is a good example of map() + lambda.

# # # # # # # # # # count howmany apple on the list

# # # # # # # # # # There are 3 "Apple" entries. 🍎

# # # # # # # # # # You can count them in Python with .count():

# # # # # # # # # # fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Mango", "Apple"]

# # # # # # # # # # print(fruits.count("Apple"))

# # # # # # # # # # Output:

# # # # # # # # # # 3

# # # # # # # # # # list.count(value) returns how many times that exact value appears in the list.

# # # # # # # # # # to text
# # # # # # # # # # fruits_list = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Mango", "Apple"]

# # # # # # # # # # # def count_non_apples(fruits):
# # # # # # # # # # #     non_apples_list = []
# # # # # # # # # # #     for f in fruits:
# # # # # # # # # # #         if f.lower() != "apple":
# # # # # # # # # # #             non_apples_list.append(f)
# # # # # # # # # # #
# # # # # # # # # # #     return non_apples_list

# # # # # # # # # # # print("Non-apples in the list: {}".format(count_non_apples(fruits_list)))
# # # # # # # # # # to text
# # # # # # # # # # def count_non_apples(fruits):
# # # # # # # # # #     non_apples_list = []
# # # # # # # # # #     for f in fruits:
# # # # # # # # # #         if f.lower() != "apple":
# # # # # # # # # #             non_apples_list.append(f)

# # # # # # # # # #     return non_apples_list

# # # # # # # # # # print("Non-apples in the list: {}".format(count_non_apples(fruits_list)))
# # # # # # # # # # from itertools import filterfalse, reduce
# # # # # # # # # # fruits_list = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Mango", "Apple"]
# # # # # # # # # # non_apples_list = filterfalse(lambda f: f.lower() == "apple", fruits_list)
# # # # # # # # # # print(list(non_apples_list))
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # from itertools import reduce

# # # # # # # # # # my_numbers = [2, 6, 4, 1, 1, 9, 3, 4]

# # # # # # # # # # def add_values(val):
# # # # # # # # # #     total = 0

# # # # # # # # # #     for v in val:
# # # # # # # # # #         total += v

# # # # # # # # # #     return total


# # # # # # # # # # print(add_values(my_numbers))


# # # # # # # # # # from functools import reduce

# # # # # # # # # # my_numbers = [2, 6, 4, 1, 1, 9, 3, 4]

# # # # # # # # # # def add_values(val1, val2):
# # # # # # # # # #     return val1 + val2

# # # # # # # # # # total = reduce(add_values, my_numbers)

# # # # # # # # # # print(total)



# # # # # # # # # # from functools import reduce

# # # # # # # # # # my_numbers = [2, 6, 4, 1, 1, 9, 3, 4]

# # # # # # # # # # total = reduce(lambda x, y: x + y, my_numbers)

# # # # # # # # # # print(total)

# # # # # # # # # # from functools import reduce

# # # # # # # # # # my_words = ["This", "is", "a", "demonstration", "of", "reduce()", "with", "strings"]

# # # # # # # # # # # result = reduce(lambda x, y: x + " " + y, my_words)
# # # # # # # # # # print(reduce(lambda a, b: f"{a} {b}", my_words))
# # # # # # # # # # print(result)


# # # # # # # # # # import random

# # # # # # # # # # unsorted_list = [45, 22, 9, 17, 89, 77, 53, 51, 19, 46]
# # # # # # # # # # unsorted_list_2 = [45, 22, 9, 17, 89, 77, 53, 51, 19, 46]

# # # # # # # # # # print(unsorted_list)

# # # # # # # # # # # in-place sort
# # # # # # # # # # unsorted_list.sort()
# # # # # # # # # # print(unsorted_list)

# # # # # # # # # # # non-destructive sort
# # # # # # # # # # print(sorted(unsorted_list_2))
# # # # # # # # # # print(sorted(unsorted_list_2, reverse=True))




# # # # # # # # # # unsorted_dict = [
# # # # # # # # # #   {
# # # # # # # # # #     "name": "John",
# # # # # # # # # #     "course": "BSIT",
# # # # # # # # # #     "grade": 70.32
# # # # # # # # # #   },
# # # # # # # # # #   {
# # # # # # # # # #     "name": "Abby",
# # # # # # # # # #     "course": "BSECE",
# # # # # # # # # #     "grade": 88.01
# # # # # # # # # #   },
# # # # # # # # # #   {
# # # # # # # # # #     "name": "Eric",
# # # # # # # # # #     "course": "BSCpE",
# # # # # # # # # #     "grade": 79.38
# # # # # # # # # #   },
# # # # # # # # # #   {
# # # # # # # # # #     "name": "John",
# # # # # # # # # #     "course": "IAC",
# # # # # # # # # #     "grade": 80.05
# # # # # # # # # #   },
# # # # # # # # # # ]



# # # # # # # # # # unsorted_dict.sort(lambda k: (k['name'], k['course']))



# # # # # # # # # # unsorted_dict = [
# # # # # # # # # #     {"name": "Abby", "course": "BSECE", "grade": 88.01},
# # # # # # # # # #     {"name": "Eric", "course": "BSCpE", "grade": 79.38},
# # # # # # # # # #     {"name": "John", "course": "BSIT", "grade": 70.32},
# # # # # # # # # #     {"name": "John", "course": "IAC", "grade": 80.05}
# # # # # # # # # # ]

# # # # # # # # # # unsorted_dict.sort(key=lambda k: (k["name"], k["grade"]))
# # # # # # # # # # unsorted_dict.sort(key=lambda k: (k["name"], k["course"]))

# # # # # # # # # # # sorted(unsorted_dict, key=lambda k: (k["name"], k["course"]))

# # # # # # # # # # print(*unsorted_dict, sep='\n')



# # # # # # # # # unsorted_multidim_list = [
# # # # # # # # #   ("John", 70.32, "BSIT"),
# # # # # # # # #   ("Abby", 88.01, "BSECE"),
# # # # # # # # #   ("Eric", 79.38, "BSCpE"),
# # # # # # # # #   ("Claire", 80.05, "IAC")
# # # # # # # # # ]
# # # # # # # # # unsorted_multidim_list.sort(key=lambda x: x[0])

# # # # # # # # # print(*unsorted_multidim_list, sep="\n")
# # # # # # # # # print()
# # # # # # # # # sorted_list = sorted(
# # # # # # # # #     unsorted_multidim_list,
# # # # # # # # #     key=lambda x: x[1]
# # # # # # # # # )
# # # # # # # # # print(*sorted_list, sep="\n")
# # # # # # # # # shapes_list = ["Rhombus", "Triangle", "Diamond", "Trapezoid", "Star"]

# # # # # # # # # shapes = map(lambda t: t + "shape", shapes_list)

# # # # # # # # # print(list(shapes))


# # # # # # # # # shapes_list = ["Rhombus", "Triangle", "Diamond", "Trapezoid", "Star"]

# # # # # # # # # # expr for list_var in iterable
# # # # # # # # # shapes = ["{}shape".format(s) for s in shapes_list]

# # # # # # # # # print(shapes)

# # # # # # # # # shapes = map(lambda t: t + "shape", shapes_list)

# # # # # # # # # print(list(shapes))



# # # # # # # # from random import randrange

# # # # # # # # # expr for list_var in iterable [if cond_expr]
# # # # # # # # # random_numbers_list = [randrange(1, 100) for _ in range(0, 10)]

# # # # # # # # # even_numbers = [x for x in random_numbers_list if x % 2 == 0]

# # # # # # # # # print(random_numbers_list)
# # # # # # # # # print(even_numbers)


# # # # # # # # # random_list_matrix = [
# # # # # # # # #     [int(randrange(1, 99)) for _ in range(0, 3)]
# # # # # # # # #     for _ in range(0, 3)
# # # # # # # # # ]

# # # # # # # # # print(random_list_matrix)


# # # # # # # # random_list_matrix = [
# # # # # # # #     tuple(int(randrange(1, 99)) for _ in range(0, 3))
# # # # # # # #     for _ in range(0, 3)
# # # # # # # # ]

# # # # # # # # print(random_list_matrix)
# # # # # # # from random import randrange

# # # # # # # # # expr for list_var in iterable [if cond_expr]
# # # # # # # random_numbers_list = [randrange(1, 100) for _ in range(0, 10)]
# # # # # # # # print(random_numbers_list)

# # # # # # # # enumerated_list = [[idx, x] for idx, x in enumerate(random_numbers_list, start=1)]
# # # # # # # enumerated_list = [{"id": idx, "value": x} for idx, x in enumerate(random_numbers_list, start=1)]

# # # # # # # print(enumerated_list)

# # # # # # # # even_numbers = [x for x in random_numbers_list if x % 2 == 0]
# # # # # # # # print(even_numbers)



# # # # # # from faker import Faker
# # # # # # from collections import namedtuple

# # # # # # # my_tuple = ("mark", 30 , f"IT trainer I",1 )


# # # # # # # my_tuple = ("Mark", 30, "IT Trainer I", 1)

# # # # # # Employee = namedtuple(
# # # # # #     "Employee",
# # # # # #     ["name", "age", "jobRole", "yearsOfWork"]
# # # # # # )

# # # # # # emp = Employee(
# # # # # #     name="Mark",
# # # # # #     age=30,
# # # # # #     jobRole="IT Trainer I",
# # # # # #     yearsOfWork=1
# # # # # # )

# # # # # # print("{}", "{}")



# # # # # from faker import Faker
# # # # # from collections import namedtuple

# # # # # f = Faker()

# # # # # # my_tuple = ("Mark", 30, "IT Trainer I", 1)

# # # # # Employee = namedtuple(
# # # # #     "Employee",
# # # # #     ["name", "age", "job_role", "years_of_work"]
# # # # # )

# # # # # emp = Employee(
# # # # #     name="Mark",
# # # # #     age=30,
# # # # #     job_role="IT Trainer I",
# # # # #     years_of_work=1
# # # # # )

# # # # # print(
# # # # #     "{} {}, {} for {} year(s)".format(
# # # # #         emp.name,
# # # # #         emp.age,
# # # # #         emp.job_role,
# # # # #         emp.years_of_work
# # # # #     )
# # # # # )
# # # # from faker import Faker
# # # # from collections import namedtuple

# # # # f = Faker()

# # # # # my_tuple = ("Mark", 30, "IT Trainer I", 1)

# # # # Employee = namedtuple(
# # # #     "Employee",
# # # #     ["name", "job_role", "age", "years_of_work"]
# # # # )
# # # # emp = Employee(
# # # #     name=f.first_name(),
# # # #     job_role="IT Trainer I",
# # # #     age=30,
# # # #     years_of_work=1
# # # # )

# # # # print(
# # # #     "{}, {} years old, {} for {} year(s)".format(
# # # #         getattr(emp, "name"),
# # # #         getattr(emp, "age"),
# # # #         getattr(emp, "job_role"),
# # # #         getattr(emp, "years_of_work")
# # # #     )
# # # # )


# # # from faker import Faker
# # # from collections import namedtuple
# # # from random import randrange

# # # f = Faker()

# # # # my_tuple = ("Mark", 30, "IT Trainer I", 1)

# # # Employee = namedtuple(
# # #     "Employee",
# # #     ["name", "age", "job_role", "years_of_work"]
# # # )

# # # # emp = Employee(
# # # #     name=f.first_name(),
# # # #     age=30,
# # # #     job_role="IT Trainer I",
# # # #     years_of_work=1
# # # # )

# # # emp_data = [
# # #     f.first_name(),
# # #     randrange(18, 35),
# # #     "IT Support L1",
# # #     randrange(1, 5)
# # # ]

# # # emp = Employee._make(emp_data)

# # # print(
# # #     "{}, {} years old. {} for {} year(s)".format(
# # #         getattr(emp, "name"),
# # #         getattr(emp, "age"),
# # #         getattr(emp, "job_role"),
# # #         getattr(emp, "years_of_work")
# # #     )
# # # )




# # # print(emp._asdict())


# # from random import randrange
# # from collections import defaultdict
# # from faker import Faker

# # f = Faker()

# # my_dict = defaultdict(lambda: "Default Value")

# # my_dict["key1"] = "value1"
# # my_dict["key2"] = None

# # print(my_dict["key1"])
# # print(my_dict["key2"])
# # print(my_dict["key3"])
# from random import randrange
# from collections import defaultdict
# from faker import Faker

# f = Faker()

# my_dict = {}
# my_dict = defaultdict(int)
# my_dict["name"] = f.first_name()
# my_dict["age"] = randrange(23, 35)
# my_dict["job_title"] = "DevOps Engineer L2"

# # my_dict = {
# #     "name": f.first_name(),
# #     "age": randrange(23, 35),
# #     "job_title": "DevOps Engineer L2"
# # }

# print(
#     "{}, {} years old, {} for {} year(s)".format(
#         my_dict["name"],
#         my_dict["age"],
#         my_dict["job_title"],
#         my_dict["years_of_work"]
#     )
# )
from random import randrange
from collections import defaultdict

fruits = [
    "Apple",
    "Banana",
    "Apple",
    "Apple",
    "Pear",
    "Orange",
    "Orange",
    "Citrus"
]

# fruit_dict = {}

# for f in fruits:
#     if f in fruit_dict:
#         fruit_dict[f] += 1
#     else:
#         fruit_dict[f] = 1

# print(fruit_dict)


fruit_dict = defaultdict(int)

for f in fruits:
    fruit_dict[f] += 1

print(fruit_dict)
