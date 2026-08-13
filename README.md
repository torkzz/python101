# Python 101 Learning Repository

Structured Python lessons, coding standards, interactive tools, and mini-projects.

---

## Table of Contents

1. [Coding Standards & Rules (`00_guidelines/`)](#1-coding-standards--rules-00_guidelines)
2. [Python Basics (`01_basics/`)](#2-python-basics-01_basics)
3. [Operators & Collections (`02_operators_and_collections/`)](#3-operators--collections-02_operators_and_collections)
4. [Control Flow & Data Processing (`03_control_flow_and_data/`)](#4-control-flow--data-processing-03_control_flow_and_data)
5. [Functional Programming (`04_functional_programming/`)](#5-functional-programming-04_functional_programming)
6. [External Libraries (`05_external_libraries/`)](#6-external-libraries-05_external_libraries)
7. [Interactive Projects (`projects/`)](#7-interactive-projects-projects)
8. [Virtual Environment & Execution](#8-virtual-environment--execution)

---

## Lesson Modules

### 1. Coding Standards & Rules (`00_guidelines/`)
- [`00_pep8_rules.py`](00_guidelines/00_pep8_rules.py): PEP 8 naming conventions, formatting, EAFP principles, and type annotations.

### 2. Python Basics (`01_basics/`)
- [`01_hello_world.py`](01_basics/01_hello_world.py): Variables, basic types (`int`, `float`, `str`, `bool`), rounding, and operators.
- [`02_interactive_inputs.py`](01_basics/02_interactive_inputs.py): Interactive console calculator and type inference tool.

### 3. Operators & Collections (`02_operators_and_collections/`)
- [`01_operators.py`](02_operators_and_collections/01_operators.py): Operator precedence (PEMDAS), floor division `//`, modulo `%`.
- [`02_builtins.py`](02_operators_and_collections/02_builtins.py): Built-in functions (`min`, `max`, `divmod`, `all`, `any`).
- [`03_iterables.py`](02_operators_and_collections/03_iterables.py): Lists, tuples, and dictionary basics.
- [`04_sets.py`](02_operators_and_collections/04_sets.py): Set creation and removing list duplicates.
- [`05_math_module.py`](02_operators_and_collections/05_math_module.py): `math` library functions (`sqrt`, `ceil`, `floor`, `factorial`).
- [`06_random_module.py`](02_operators_and_collections/06_random_module.py): `random` library usage (`randint`, `choice`, `shuffle`).
- [`07_strings.py`](02_operators_and_collections/07_strings.py): String methods (`strip`, casing, searching).
- [`08_dict_deep_dive.py`](02_operators_and_collections/08_dict_deep_dive.py): Dict methods (`get`, `setdefault`), merge operator `|`, and dict comprehensions.
- [`09_interactive_gradebook.py`](02_operators_and_collections/09_interactive_gradebook.py): CLI Gradebook app using dicts and sets.

### 4. Control Flow & Data Processing (`03_control_flow_and_data/`)
- [`01_control_flow.py`](03_control_flow_and_data/01_control_flow.py): `enumerate()`, generator functions (`yield`), list comprehensions.
- [`02_regex_and_json.py`](03_control_flow_and_data/02_regex_and_json.py): Regular expressions (`re`) and JSON serialization (`json`).

### 5. Functional Programming (`04_functional_programming/`)
- [`01_lambdas.py`](04_functional_programming/01_lambdas.py): Lambda syntax, default parameters, `map()`, and `filter()`.

### 6. External Libraries (`05_external_libraries/`)
- [`01_faker_basics.py`](05_external_libraries/01_faker_basics.py): Mock data generation with `faker` and nested dict structures.

### 7. Interactive Projects (`projects/`)
- [`interactive_quiz.py`](projects/interactive_quiz.py): CLI multiple-choice quiz game.
- [`number_guessing.py`](projects/number_guessing.py): Configurable difficulty number guessing game.
- [`cmatrix.py`](projects/cmatrix.py): Terminal Matrix rain animation.

---

## 8. Virtual Environment & Execution

Run modules directly using `python3` or the virtualenv interpreter:

```bash
# Coding guidelines example
python3 00_guidelines/00_pep8_rules.py

# Interactive Type Inspector
python3 01_basics/02_interactive_inputs.py

# Student Gradebook
python3 02_operators_and_collections/09_interactive_gradebook.py

# Faker integration (requires venv dependencies)
./pyproject/.venv/bin/python3 05_external_libraries/01_faker_basics.py

# Quiz project
python3 projects/interactive_quiz.py
```
