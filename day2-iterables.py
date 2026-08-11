# Different Types of Iterables

# An iterable is any Python object capable of returning its elements one at a time.

# Examples of iterables:

# • Strings: "hello"

# • Lists: [1, 2, 3]

# • Tuples: (1, 2, 3)

# • Ranges: range(5)

# • Dictionaries: {"key": "value"}

# • Sets: {1, 2, 3}


## Lists in Python

# ```text
# Lists

# A list is a mutable sequence of objects.
# It is a collection of elements that is ordered and changeable.

# A sequence is an ordered collection — that is, each element in the
# collection has its own place in some ordering.
# ```

# ### How to write a list in Python

# ```python
# # A list of strings
# thislist = ['apple', 'banana', 'cherry']
# print(thislist)
# ```

# Output:

# ```text
# ['apple', 'banana', 'cherry']
# ```

# ```python
# # A list of numbers
# scores = [74, 82, 78, 99, 83, 91, 77, 98, 74, 87]
# print(scores)
# ```

# ```python
# # A list can contain different types
# mixed = ['cheese', 0.1, 5, True]
# print(mixed)
# ```

# Output:

# ```text
# ['cheese', 0.1, 5, True]
# ```

# ### Empty list

# A list doesn't have to contain anything:

# ```python
# aint_nothing_here = []

# print(aint_nothing_here)
# ```

# Output:

# ```text
# []
# ```

# ### Key concepts 🧠

# **Ordered** means the elements have positions:

# ```python
# fruits = ['apple', 'banana', 'cherry']
# ```

# ```text
# apple  → position 0
# banana → position 1
# cherry → position 2
# ```

# **Mutable** means you can change the list after creating it:

# ```python
# fruits = ['apple', 'banana', 'cherry']

# fruits[0] = 'orange'

# print(fruits)
# ```

# Output:

# ```text
# ['orange', 'banana', 'cherry']
# ```

# So remember:

# > **List = ordered + changeable collection of objects.**
# Accessing individual element in a list

# Lists are ordered. This allows us to access individual elements within a list using an
# index. An index is just a number that corresponds to an element's position within a
# list.

# list:       4.2    9.5    1.1    3.1    2.9    8.5    3.5    1.4    1.9    3.3
# Index (+):   0      1      2      3      4      5      6      7      8      9
# Index (-): -10     -9     -8     -7     -6     -5     -4     -3     -2     -1


# my_list = [4.2, 9.5, 1.1, 3.1, 2.9, 8.5, 3.5, 1.4, 1.9, 3.3]


# print(my_list[-1])
# [OUT]: 3.3

# print(my_list[0])
# [OUT]: 4.2


# print(my_list[-8])
# [OUT]: 1.1

# print(my_list[9])
# [OUT]: 3.3


# Slicing elements in a list

# Slicing lets you extract sublists from a list using the syntax:

# • list[start:end:step]
# • start: index where slice begins (inclusive).
# • end: index where slice ends (exclusive).
# • step: how many elements to skip (default = 1).

# list:       4.2    9.5    1.1    3.1    2.9    8.5    3.5    1.4    1.9    3.3
# Index (+):   0      1      2      3      4      5      6      7      8      9
# Index (-): -10     -9     -8     -7     -6     -5     -4     -3     -2     -1


# Slicing elements in a list

# # Syntax: list[start:end:step]

# my_list = [4.2, 9.5, 1.1, 3.1, 2.9, 8.5, 3.5, 1.4, 1.9, 3.3]

# # Basic slicing
# print(my_list)
# print("[0:2]" ,my_list[0:2])    # Elements from index 0 to 1
# print("[2:5]" ,my_list[2:5])    # Elements from index 2 to 4
# print("[:3])" ,my_list[:3])     # From start to index 2
# print("[3:])" ,my_list[3:])     # From index 3 to end
# print("[:]) " ,my_list[:])      # Whole list


# Modifying the values of individual elements in a list

# Syntax: list[start:end:step]

# my_list = [4.2, 9.5, 1.1, 3.1, 2.9, 8.5, 3.5, 1.4, 1.9, 3.3]

# my_list[0] = "new value"       # Change the value of index 0
# print(my_list)

# # Change the values of index 1 and 2
# my_list[1:3] = ["new value", "c"]

# print(my_list)
# Modifying the values of individual elements in a list

# Syntax: list[start:end:step]

# my_list = [4.2, 9.5, 1.1, 3.1, 2.9, 8.5, 3.5, 1.4, 1.9, 3.3]

# # The replacement sequence does not have to match
# # the slice length.
# # Slice assignment can shrink or expand a list.

# my_list[1:5] = ["new value", "c"]   # Change 4 elements with 2 elements
# print(my_list)

# my_list[1:3] = ["a", "b", "c", "d"]  # Replace 2 elements with 4 elements
# print(my_list)

# my_list = [24,False, True, False, False, True]

# print(sum(my_list))


# numbers: list[int] = [10, 20, 30]
# numbers.append("one")

# print(numbers)


# Some convenient built-in functions that work with lists

# description                     constraint(s) if any              example

# sum()    calculates sum of      values must be numeric or        sum(data)
#          elements               Boolean *

# len()    returns number of      none                             len(data)
#          elements


# max()    returns largest        can't mix numerics and          max(data)
#          value                  strings;
#                                 must be all numeric or all
#                                 strings

# min()    returns smallest       can't mix numerics and          min(data)
#          value                  strings;
#                                 must be all numeric or all
#                                 strings


# my_list = [4.2, 9.5, 1.1, 3.1, 2.9, 8.5, 3.5, 1.4, 1.9, 3.3]

# print(sum(my_list))
# # [OUT]: 39.4

# print(len(my_list))
# # [OUT]: 10

# print(max(my_list))
# # [OUT]: 9.5

# print(min(my_list))
# # [OUT]: 1.1


# Other List Methods

# l.index(x)
# Returns the index of the first occurrence of the element in the list.

# l.reverse()
# Reverses all the elements in the list.

# l.remove(x)
# Removes the first occurrence of the element in the element.

# l.insert(x, y)
# Insert a new element at the specific index.

# l.clear()
# Remove all the elements from the list.

# l.extend(x, y)
# Appends any number of elements to the end of the list.


# my_list = [1, 2, 3, 4, 5]
# print(my_list.index(4))
# # [OUT]: 3


# my_list.reverse()
# print(my_list)
# # [OUT]: [5, 4, 3, 2, 1]


# my_list.remove(3)
# print(my_list)
# # [OUT]: [1, 2, 4, 5]


# my_list.insert(2, 'three')
# print(my_list)
# # [OUT]: [1, 2, 'three', 4, 5]


# my_list.clear()
# print(my_list)
# # [OUT]: []


# my_list.extend([6, 7, 8])
# print(my_list)
# [OUT]: [1, 2, 3, 4, 5, 6, 7, 8]


# How to write a tuple in Python

# The crucial thing in writing a tuple is commas (,) — we separate elements of a tuple
# with commas — but it's conventional to write them with parentheses () as well.


coordinates = 0.378, 0.911          # Create a tuple with a comma without ()
print(coordinates)
# [OUT]: (0.378, 0.911)


coordinates = (0.378, 0.911)       # Create a tuple with a comma with ()
print(coordinates)
# [OUT]: (0.378, 0.911)


singleton = 5,                     # Create a tuple with a single element with a comma without ()
print(singleton)
# [OUT]: (5,)


singleton = ('Hovercraft',)        # Create a tuple with a single element with a comma
print(singleton)                   # with ()
# [OUT]: ('Hovercraft',)



# Remember for Tuple

# • Working with tuples is in many ways similar to working with lists.

# • They support indexing and slicing, and they are fully compatible with several
#   useful built-in functions such as len(), sum(), max(), and min().

# • However, unlike lists, tuples are immutable. This means that once a tuple is
#   created, its contents cannot be changed.

# • As a result, tuples do not support modification methods such as .append(),
#   .insert(), .pop(), .remove(), or .sort(). Attempting to use these methods on a tuple
#   will result in an error.


# What about a tuple that contains a list?

# As with lists, we can access the elements of a tuple with index.

# Note: Even though tuples are immutable, the lists inside them are mutable.


# t = ([1, 2, 3], [4, 5, 6])          # tuple that contains a list
# print(t)

# [OUT]: ([1, 2, 3], [4, 5, 6])


# t[0][1] = 5                         # first index: tuple; second index: list
# print(t)                            # in the tuple, then modify its second element
# print(t)                            # modifies the first element of the first list inside the tuple

# [OUT]: ([1, 5, 3], [4, 5, 6])


# Visualizing a tuple with a list

# index of the list inside tuple
#         ↓
#         0   1   2       0   1   2
#         ↓   ↓   ↓       ↓   ↓   ↓
#        [ 1   2   3 ]   [ 4   5   6 ]
#         └───────┘       └───────┘
#              0               1
#              └──── index of tuple ────┘




# How to create a dictionary in Python

# The entries of a dictionary appear within braces {}. A colon (:) that separates the
# key/value pairs.

# Note: Keys must be unique within a dictionary.


dictionary = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}


# Can be formatted as follows for readability
dictionary = {
    'food': 'Spam',
    'quantity': 4,
    'color': 'pink'
}

print(dictionary)

# [OUT]: {'food': 'Spam', 'quantity': 4, 'color': 'pink'}


# How to create a dictionary in Python

# Also, take note, that the dict() function can create a dictionary from other sequences.


# From a list of lists to a dictionary
pairs = [["country", "Philippines"], ["currency", "Peso"]]
info = dict(pairs)
print(info)

# [OUT]: {'country': 'Philippines', 'currency': 'Peso'}


# From a tuple of tuples to a dictionary
pairs = (("brand", "Toyota"), ("model", "Corolla"), ("year", 2022))
car = dict(pairs)
print(car)

# [OUT]: {'brand': 'Toyota', 'model': 'Corolla', 'year': 2022}


# From a list of tuples to a dictionary
my_list = [("apple", 2), ("banana", 3), ("orange", 4)]
my_dict = dict(my_list)
print(my_dict)

# [OUT]: {'apple': 2, 'banana': 3, 'orange': 4}


# Accessing elements in a dictionary

# • Square bracket notation: Square brackets [] with the key inside access the value
#   associated with that key. If the key is not found, an exception will be thrown.

# • get() method: The get() method is called with the key as an argument to access
#   the value associated with that key. If the key is not found, the method returns
#   None by default.


# # dictionary = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# print(dictionary['food'])
# # [OUT]: Spam

# print(dictionary['quantity'])
# # [OUT]: 4

# print(dictionary['color'])
# # [OUT]: pink

# print(dictionary['name'])
# # [OUT]: TypeError

# print(dictionary.get('food'))
# # [OUT]: Spam

# print(dictionary.get('name'))
# # [OUT]: None





employee = {
    "name": "Kevin",
    "age": 25
}

email = employee.get("email", "not provided")

print(email)

if email is None:
    print("The email key does not exist.")
else:
    print("Email:", email)
