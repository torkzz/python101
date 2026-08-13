"""
PEP 8 & Pythonic Coding Guidelines Summary

1. Naming Standards:
   - Module/File: snake_case (e.g. interactive_quiz.py)
   - Function/Var: snake_case (e.g. calculate_total)
   - Constant: ALL_CAPS (e.g. MAX_LIMIT)
   - Class: PascalCase (e.g. UserProfileManager)

2. Formatting:
   - 4 spaces per indentation level.
   - Max 79 characters line length.
   - 2 blank lines between top-level functions/classes.
   - 1 blank line between methods inside a class.

3. Pythonic Rules:
   - Prefer EAFP (dict.get(), try-except) over defensive checks.
   - Use 'with' context manager for files and network resources.
   - Use PEP 484 Type Annotations for functions.
"""

import sys
from typing import Optional


class UserSession:
    """Example class adhering to PEP 8 standards."""

    def __init__(self, username: str) -> None:
        self.username: str = username

    def get_display_name(self) -> str:
        return self.username.title()


def calculate_average(scores: list[float]) -> float:
    """Calculate average of float scores safely."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def safe_get_user(user_map: dict[str, str], user_id: str) -> Optional[str]:
    """Demonstrates EAFP approach with dict getter."""
    return user_map.get(user_id)


def main() -> None:
    session = UserSession("alex")
    print(f"User: {session.get_display_name()}")
    
    scores = [88.5, 92.0, 79.5]
    print(f"Average score: {calculate_average(scores):.2f}")


if __name__ == "__main__":
    main()
