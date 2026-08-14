"""
Object-Oriented Programming (OOP): Encapsulation, Properties & Static Methods

Concepts:
- Private attributes convention (`_attribute`).
- Name mangling (`__attribute`).
- Property Decorators (`@property` getter and `@name.setter`).
- Utility methods (`@staticmethod`).
"""

from faker import Faker


class Person:
    """Demonstrates properties, protected attributes, and static methods."""

    def __init__(self, name: str = "", age: int = 0) -> None:
        self._name: str = name       # Protected attribute
        self._age: int = age         # Protected attribute
        self.__secret_id: str = "SECRET_123"  # Private (name mangled) attribute
        self.faker: Faker = Faker()

    # Getter for name
    @property
    def name(self) -> str:
        return self._name

    # Setter for name
    @name.setter
    def name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name

    # Getter for age
    @property
    def age(self) -> int:
        return self._age

    # Setter for age
    @age.setter
    def age(self, age: int) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = age

    def generate_random_name(self) -> str:
        """Internal method utilizing Faker instance."""
        return self.faker.first_name()

    @staticmethod
    def generate_japanese_name() -> str:
        """Static method independent of instance state."""
        f_ja = Faker("ja-JP")
        return f_ja.first_kana_name()


class Student(Person):
    """Subclass inheriting from Person."""

    def __init__(self, name: str = "", age: int = 0, course: str = "BSIT") -> None:
        super().__init__(name, age)
        self._course: str = course
        self._year_level: int = 1

    @property
    def course(self) -> str:
        return self._course

    @course.setter
    def course(self, course: str) -> None:
        self._course = course


def main() -> None:
    print("=== OOP Encapsulation & Properties Demo ===")
    student = Student()

    # Using @property setters
    student.name = student.generate_random_name()
    student.age = 20
    student.course = "BSCpE"

    # Using @property getters
    print(f"Student Name: {student.name}")
    print(f"Student Age : {student.age}")
    print(f"Course      : {student.course}")

    # Calling @staticmethod
    print(f"Japanese Name (StaticMethod): {Person.generate_japanese_name()}")


if __name__ == "__main__":
    main()
