"""
Object-Oriented Programming (OOP): Abstract Base Classes (ABC)

Concepts:
- Abstract Base Classes (`from abc import ABC, abstractmethod`).
- Contract enforcement: Subclasses MUST implement all `@abstractmethod` methods.
- Attempting to instantiate an abstract class raises `TypeError`.
- Concrete implementations inheriting from an ABC interface.
"""

from abc import ABC, abstractmethod
import random


class StudentOperations(ABC):
    """Abstract Interface defining required operations for student management."""

    @abstractmethod
    def set_courses(self, *args: str) -> None:
        """Assign one or more courses to the student."""
        pass

    @abstractmethod
    def list_courses(self) -> list[str]:
        """Return the list of assigned courses."""
        pass

    @abstractmethod
    def generate_student_id(self) -> str:
        """Generate a unique student identifier."""
        pass


class CollegeStudent(StudentOperations):
    """Concrete implementation of StudentOperations contract."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.courses: list[str] = []
        self.student_id: str = self.generate_student_id()

    def set_courses(self, *args: str) -> None:
        """Implement set_courses with variable positional arguments (*args)."""
        self.courses.extend(args)

    def list_courses(self) -> list[str]:
        """Implement list_courses returning list of string courses."""
        return self.courses

    def generate_student_id(self) -> str:
        """Implement unique student ID generation."""
        random_num = random.randint(1000, 9999)
        return f"CS-2026-{random_num}"


def main() -> None:
    print("=== Abstract Base Class (ABC) Demo ===")

    # 1. Attempting to instantiate Abstract Base Class directly raises TypeError
    try:
        abstract_obj = StudentOperations()  # type: ignore
    except TypeError as e:
        print(f"Cannot instantiate ABC directly: {e}")

    # 2. Instantiating Concrete Subclass
    student = CollegeStudent("Alex Rivera")
    student.set_courses("Python Programming", "Database Systems", "Data Structures")

    print(f"\nStudent Name: {student.name}")
    print(f"Student ID  : {student.student_id}")
    print("Enrolled Courses:")
    for course in student.list_courses():
        print(f"  - {course}")


if __name__ == "__main__":
    main()
