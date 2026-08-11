# How to create a set in Python

# Set is defined using curly braces { } or the set() constructor.

# Note: Duplicate values will be ignored.


# Using curly braces
this_set1 = {"apple", "banana", "cherry"}
print(this_set1)

# [OUT]: {'banana', 'apple', 'cherry'}


# Using set() constructor
number_list = set([10, 3, 7, 1, 5])
print(number_list)

# [OUT]: {1, 3, 5, 7, 10}


this_set2 = {"orange", "banana", "cherry", "banana"}  # set with duplicates
print(this_set2)                                      # duplicates will be ignored

# [OUT]: {'orange', 'banana', 'cherry'}


# How to create a set in Python

# Set is defined using curly braces { } or the set() constructor.

# Note: Duplicate values will be ignored.


# Using curly braces
this_set1 = {"apple", "banana", "cherry"}
print(this_set1)

# [OUT]: {'banana', 'apple', 'cherry'}


# Using set() constructor
number_list = set([10, 3, 7, 1, 5])
print(number_list)

# [OUT]: {1, 3, 5, 7, 10}


this_set2 = {"orange", "banana", "cherry", "banana"}  # set with duplicates
print(this_set2)                                      # duplicates will be ignored

# [OUT]: {'orange', 'banana', 'cherry'}


# Using sets to remove duplicates in lists

# Duplicate elements in a list
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))    # set() removes the duplicate elements

print(unique_numbers)                  # list() converts the set back into the list

# [OUT]: [2, 3, 1, 4, 5]                 # duplicates are removed, but the order is not guaranteed
fruits = {"apple", "banana", "cherry", "banana"}

print(fruits)
print(type(fruits))

employees = ["Kevin Paul", "Gem", "Anja", "John", "Anja"]

unique_employees = set(employees)

print(employees.count("Kevin Paul"))
print(employees.count("Anja"))

duplicate_count = len(employees) - len(set(employees))

print(duplicate_count)

print(unique_employees)
