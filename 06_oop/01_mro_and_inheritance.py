"""
Object-Oriented Programming (OOP): Multiple Inheritance & Method Resolution Order (MRO)

Concepts:
- Multiple inheritance syntax `class Child(Parent1, Parent2):`.
- Method Resolution Order (MRO): Left-to-right search order in parent list.
- Method lookup rule:
    1. Search child class first.
    2. Search first parent class (leftmost).
    3. Search next parent classes linearly.
    4. Continue until method is found in the inheritance chain.
- Inspecting resolution order using `Class.mro()` or `Class.__mro__`.
"""


class First:
    def dupe_func(self):
        print("Dupe function from First class")

    def other_func(self):
        print("Other function from First class")


class Second:
    def dupe_func(self):
        print("Dupe function from Second class")


# Class Third inherits from Second (1st parent) and First (2nd parent)
class Third(Second, First):
    def __init__(self):
        super().__init__()
        print("Third class initialized")

        # super().dupe_func() resolves to Second.dupe_func() due to MRO order (Second, First)
        super().dupe_func()

        # super().other_func() resolves to First.other_func() because Second doesn't have it
        super().other_func()


def main():
    print("=== MRO (Method Resolution Order) Demo ===")
    t = Third()

    print("\n=== MRO Inheritance Order Inspection ===")
    # Third.__mro__ returns tuple showing exact search order
    for idx, cls in enumerate(Third.mro(), start=1):
        print(f"  {idx}. {cls.__name__}")


if __name__ == "__main__":
    main()
