# # # # # # # from random import randrange
# # # # # from collections import defaultdict

# # # # # # # expenses = [
# # # # # # #     ("Groceries", 1940.33),
# # # # # # #     ("Lunch", 180.00),
# # # # # # #     ("Utilities", 2000.00),
# # # # # # #     ("Groceries", 1366.25),
# # # # # # #     ("Utilities", 1600.00),
# # # # # # #     ("Lunch", 200.00)
# # # # # # # ]

# # # # # # # enumerated_expenses = [
# # # # # # #     [idx, expense]
# # # # # # #     for idx, expense in enumerate(expenses, start=1)
# # # # # # # ]

# # # # # # # print(*enumerated_expenses)


# # # # # # from collections import defaultdict

# # # # # # expenses = [("Groceries", 1940.33), ("Lunch", 180.00), ("Utilities", 2000.00),
# # # # # #             ("Groceries", 1366.25), ("Utilities", 1600.00), ("Lunch", 200.00)]

# # # # # # agg = defaultdict(float)
# # # # # # for (category, amount) in expenses:
# # # # # #     agg[category] += amount

# # # # # # print(dict(agg))
# # # # # employees = {
# # # # #     "Liz": "HR",
# # # # #     "Abby": "Internal Support I",
# # # # #     "Jun": "HR",
# # # # #     "Ely": "Supervisor",
# # # # #     "Marie": "Internal Support I",
# # # # #     "Jules": "HR",
# # # # #     "Arnold": "Supervisor"
# # # # # }

# # # # # employee_assignments = defaultdict(list)

# # # # # for k, v in employees.items():
# # # # #     # {"HR": ["Liz", "Jun", "Jules"]}
# # # # #     employee_assignments[v].append(k)
# # # # #     print(dict(employee_assignments))
# # # # from collections import OrderedDict

# # # # my_dict = {
# # # #     "one": 1,
# # # #     "two": 2,
# # # #     "three": 3,
# # # #     "four": 4
# # # # }

# # # # od = OrderedDict(my_dict)
# # # # od["five"] = 5
# # # # print(dict(od))
# # # # del(od["two"])
# # # # print(dict(od))
# # # # od.move_to_end("one")
# # # # print(dict(od))


# # # # od.popitem(last=False)
# # # # print(dict(od))

# # # # od["two"] = "II"
# # # # od.move_to_end("two", last=False)
# # # # print(dict(od))
# # # # If you mean Python's **`deque` (double-ended queue)**, import it from `collections`:

# # # # ```python
# # # # from collections import deque
# # # # ```

# # # # ### Basic example

# # # # ```python
# # # # from collections import deque

# # # # my_deque = deque(["A", "B", "C"])

# # # # print(my_deque)
# # # # ```

# # # # Output:

# # # # ```text
# # # # deque(['A', 'B', 'C'])
# # # # ```

# # # # ### Add to either end

# # # # ```python
# # # # my_deque.append("D")       # right side
# # # # my_deque.appendleft("Z")   # left side

# # # # print(my_deque)
# # # # ```

# # # # ```text
# # # # deque(['Z', 'A', 'B', 'C', 'D'])
# # # # ```

# # # # ### Remove from either end

# # # # ```python
# # # # my_deque.pop()       # removes D
# # # # my_deque.popleft()   # removes Z
# # # # ```

# # # # ### Think of it like this

# # # # ```text
# # # # appendleft()  ← [ A ][ B ][ C ] →  append()
# # # # popleft()     → [ A ][ B ][ C ] ←  pop()
# # # # ```

# # # # A `deque` is particularly useful when you need **fast insertion/removal from both ends**.

# # # # For example, a queue:

# # # # ```python
# # # # from collections import deque

# # # # queue = deque()

# # # # queue.append("Kevin")
# # # # queue.append("John")
# # # # queue.append("Mary")

# # # # print(queue.popleft())  # Kevin
# # # # print(queue.popleft())  # John
# # # # ```

# # # # Unlike doing `list.pop(0)`, `deque.popleft()` is designed for this use case and is **O(1)**.
# # # from collections import deque

# # # fruits = ["Apple", "Banana", "Cherry", "Durian"]

# # # my_deque = deque(fruits, maxlen=10)

# # # print(my_deque)

# # # my_deque.append("Strawberry")
# # # my_deque.appendleft("Coconut")
# # # print(my_deque)

# # # my_deque.insert(4, "Cacao")
# # # print(my_deque)
# # # print(my_deque)

# # # my_deque.insert(4, "Cacao")
# # # print(my_deque)

# # # my_deque.append("Apple")
# # # print(my_deque)

# # # print(my_deque.count("Apple"))

# # # print(my_deque.pop())
# # # print(my_deque.popleft())
# # # print(my_deque)


# # from collections import deque

# # fruits = ["Apple", "Banana", "Cherry", "Durian"]

# # my_deque = deque(fruits, maxlen=10)

# # print(my_deque)

# # my_deque.append("Strawberry")
# # my_deque.appendleft("Coconut")
# # print(my_deque)

# # my_deque.insert(4, "Cacao")
# # print(my_deque)

# # my_deque.insert(4, "Cacao")
# # print(my_deque)

# # my_deque.append("Apple")
# # print(my_deque)

# # print(my_deque.count("Apple"))

# # print(my_deque.pop())
# # print(my_deque.popleft())
# # print(my_deque)

# # my_deque.remove("Apple")
# # print(my_deque)

# # my_deque.extend(["Rambutan", "Chico", "Guava"])
# # print(my_deque)

# # my_deque.rotate(3)
# # print(my_deque)



# from collections import deque

# fruits = ["Apple", "Banana", "Cherry", "Durian"]
# my_deque = deque(fruits, maxlen=10)

# print(my_deque)

# my_deque.append("Strawberry")
# my_deque.appendleft("Coconut")
# print(my_deque)

# my_deque.insert(4,"Cacao")
# print(my_deque)

# my_deque.append("Apple")
# print(my_deque)
# print(my_deque.count("Apple"))

# print(my_deque.pop())
# print(my_deque.popleft())
# print(my_deque)

# my_deque.remove("Apple")
# print(my_deque)

# my_deque.extend(["Rambutan", "Chico", "Guava"])
# print(my_deque)

# my_deque.rotate(-3)
# print(my_deque)

# my_deque.reverse()
# print(my_deque)

# print(len(my_deque))
# my_deque.extend(["Orange", "Grapes", "Kiwi", "Peach"])

# my_deque.clear()


#argument packing and unpacking
#
