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
    "3": ("00_guidelines/02_docstrings_and_tricks.py", "Docstrings (PEP 257) & Language Tricks"),
    "4": ("01_basics/01_hello_world.py", "Basics: Data Types & Operators"),
    "5": ("01_basics/02_interactive_inputs.py", "Interactive Calculator & Type Inspector"),
    "6": ("02_operators_and_collections/08_dict_deep_dive.py", "Dict Deep Dive"),
    "7": ("02_operators_and_collections/09_interactive_gradebook.py", "CLI Student Gradebook"),
    "8": ("02_operators_and_collections/10_deque_collections.py", "Deque (Double-Ended Queue)"),
    "9": ("03_control_flow_and_data/01_control_flow.py", "Control Flow & Generators"),
    "10": ("03_control_flow_and_data/02_regex_and_json.py", "Regex & JSON Handling"),
    "11": ("03_control_flow_and_data/03_csv_and_match_case.py", "CSV Parsing & Match/Case"),
    "12": ("03_control_flow_and_data/04_sqlite_basics.py", "SQLite Queries & Fetch Methods"),
    "13": ("03_control_flow_and_data/05_asyncio_basics.py", "Asyncio Non-Blocking I/O & to_thread()"),
    "14": ("03_control_flow_and_data/06_exceptions_handling.py", "Exception Handling (try/except/else/finally)"),
    "15": ("03_control_flow_and_data/07_file_io_basics.py", "File I/O Operations & pathlib.Path"),
    "16": ("04_functional_programming/01_lambdas.py", "Lambda Functions & Map/Filter"),
    "17": ("04_functional_programming/02_args_and_kwargs.py", "Packing & Unpacking (*args, **kwargs)"),
    "18": ("04_functional_programming/03_decorators_basics.py", "Decorators Basics (@decorator_method & inner_method)"),
    "19": ("04_functional_programming/04_decorators_with_args.py", "Decorators with Arguments (@two_values & multiply_values)"),
    "20": ("04_functional_programming/05_logging_decorators.py", "Logging Module & Prepend Decorator (@prepend_log)"),
    "21": ("05_external_libraries/01_faker_basics.py", "External Libraries: Faker"),
    "22": ("05_external_libraries/02_csv_writing_with_faker.py", "Writing CSV with Faker (writer & DictWriter)"),
    "23": ("05_external_libraries/03_sqlite_faker_inserts.py", "SQLite Schema Creation & Faker Population"),
    "24": ("05_external_libraries/04_requests_http_basics.py", "HTTP Requests (GET, POST, Headers & JSON)"),
    "25": ("05_external_libraries/05_api_deck_of_cards.py", "REST API Integration (Deck of Cards API)"),
    "26": ("05_external_libraries/06_aiohttp_async_requests.py", "Native Async HTTP Client (aiohttp & ClientSession)"),
    "27": ("05_external_libraries/07_web_scraping_bs4.py", "Web Scraping with BeautifulSoup4 (bs4)"),
    "28": ("06_oop/01_mro_and_inheritance.py", "OOP Multiple Inheritance & MRO"),
    "29": ("06_oop/02_abstract_classes.py", "OOP Abstract Base Classes (ABC & @abstractmethod)"),
    "30": ("06_oop/03_properties_and_encapsulation.py", "OOP Properties & Encapsulation (@property & @staticmethod)"),
    "31": ("07_testing/01_unittest_basics.py", "Unit Testing Basics (unittest & TestCase)"),
    "32": ("07_testing/02_unittest_assertions.py", "Unittest Assertion Methods Cheat Sheet"),
    "33": ("08_aws_cloud/01_lambda_handler_basics.py", "AWS Lambda Function Handler Structure (boto3 & event/context)"),
    "34": ("projects/interactive_quiz.py", "Interactive Quiz App"),
    "35": ("projects/number_guessing.py", "Number Guessing Game"),
    "36": ("projects/blackjack.py", "CLI Blackjack Card Game"),
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
