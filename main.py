"""
Main Entrypoint / Interactive CLI Navigator for Python 101 Modules
"""

import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

MODULES = {
    "1": ("00_guidelines/00_pep8_rules.py", "PEP 8 Rules & Guidelines"),
    "2": ("00_guidelines/01_venv_setup.py", "Venv & Requirements Inspector"),
    "3": ("01_basics/01_hello_world.py", "Basics: Data Types & Operators"),
    "4": ("01_basics/02_interactive_inputs.py", "Interactive Calculator & Type Inspector"),
    "5": ("02_operators_and_collections/08_dict_deep_dive.py", "Dict Deep Dive"),
    "6": ("02_operators_and_collections/09_interactive_gradebook.py", "CLI Student Gradebook"),
    "7": ("02_operators_and_collections/10_deque_collections.py", "Deque (Double-Ended Queue)"),
    "8": ("03_control_flow_and_data/01_control_flow.py", "Control Flow & Generators"),
    "9": ("03_control_flow_and_data/02_regex_and_json.py", "Regex & JSON Handling"),
    "10": ("03_control_flow_and_data/03_csv_and_match_case.py", "CSV Parsing & Match/Case"),
    "11": ("03_control_flow_and_data/04_sqlite_basics.py", "SQLite Queries & Fetch Methods"),
    "12": ("04_functional_programming/01_lambdas.py", "Lambda Functions & Map/Filter"),
    "13": ("04_functional_programming/02_args_and_kwargs.py", "Packing & Unpacking (*args, **kwargs)"),
    "14": ("05_external_libraries/01_faker_basics.py", "External Libraries: Faker"),
    "15": ("05_external_libraries/02_csv_writing_with_faker.py", "Writing CSV with Faker (writer & DictWriter)"),
    "16": ("05_external_libraries/03_sqlite_faker_inserts.py", "SQLite Schema Creation & Faker Population"),
    "17": ("projects/interactive_quiz.py", "Interactive Quiz App"),
    "18": ("projects/number_guessing.py", "Number Guessing Game"),
}


def run_module(relative_path: str) -> None:
    """Executes target script with current Python interpreter."""
    target_path = ROOT_DIR / relative_path
    if not target_path.exists():
        print(f"Error: File not found ({target_path})")
        return

    print(f"\n--- Running {relative_path} ---\n")
    subprocess.run([sys.executable, str(target_path)])


def main() -> None:
    while True:
        print("\n=== Python 101 Learning Modules ===")
        for key, (_, title) in MODULES.items():
            print(f"{key:>2}. {title}")
        print(" q. Exit")

        choice = input("\nSelect module to run: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        if choice in MODULES:
            rel_path, _ = MODULES[choice]
            run_module(rel_path)
        else:
            print("Invalid selection, try again.")


if __name__ == "__main__":
    main()
