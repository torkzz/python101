# Python 101 Learning Repository

Structured Python lessons, coding standards, interactive tools, and mini-projects.

---

## Quick Start

Launch the interactive repository navigator:

```bash
python3 main.py
```

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Coding Standards & Guidelines (`00_guidelines/`)](#2-coding-standards--guidelines-00_guidelines)
3. [Python Basics (`01_basics/`)](#3-python-basics-01_basics)
4. [Operators & Collections (`02_operators_and_collections/`)](#4-operators--collections-02_operators_and_collections)
5. [Control Flow & Data Processing (`03_control_flow_and_data/`)](#5-control-flow--data-processing-03_control_flow_and_data)
6. [Functional Programming (`04_functional_programming/`)](#6-functional-programming-04_functional_programming)
7. [External Libraries (`05_external_libraries/`)](#7-external-libraries-05_external_libraries)
8. [Interactive Projects (`projects/`)](#8-interactive-projects-projects)

---

## Lesson Modules

### 2. Coding Standards & Guidelines (`00_guidelines/`)
- [`00_pep8_rules.py`](00_guidelines/00_pep8_rules.py): PEP 8 naming conventions, formatting, EAFP principles, and type annotations.
- [`01_venv_setup.py`](00_guidelines/01_venv_setup.py): Virtual environment (`venv`) creation, activation, `pip` package installation, and execution inspection.

### 3. Python Basics (`01_basics/`)
- [`01_hello_world.py`](01_basics/01_hello_world.py): Variables, basic types (`int`, `float`, `str`, `bool`), rounding, and operators.
- [`02_interactive_inputs.py`](01_basics/02_interactive_inputs.py): Interactive console calculator and type inference tool.

### 4. Operators & Collections (`02_operators_and_collections/`)
- [`01_operators.py`](02_operators_and_collections/01_operators.py): Operator precedence (PEMDAS), floor division `//`, modulo `%`.
- [`02_builtins.py`](02_operators_and_collections/02_builtins.py): Built-in functions (`min`, `max`, `divmod`, `all`, `any`).
- [`03_iterables.py`](02_operators_and_collections/03_iterables.py): Lists, tuples, and dictionary basics.
- [`04_sets.py`](02_operators_and_collections/04_sets.py): Set creation and removing list duplicates.
- [`05_math_module.py`](02_operators_and_collections/05_math_module.py): `math` library functions (`sqrt`, `ceil`, `floor`, `factorial`).
- [`06_random_module.py`](02_operators_and_collections/06_random_module.py): `random` library usage (`randint`, `choice`, `shuffle`).
- [`07_strings.py`](02_operators_and_collections/07_strings.py): String methods (`strip`, casing, searching, `[start:stop:step]` slicing).
- [`08_dict_deep_dive.py`](02_operators_and_collections/08_dict_deep_dive.py): Dict methods (`get`, `setdefault`), merge operator `|`, and dict comprehensions.
- [`09_interactive_gradebook.py`](02_operators_and_collections/09_interactive_gradebook.py): CLI Gradebook app using dicts and sets.
- [`10_deque_collections.py`](02_operators_and_collections/10_deque_collections.py): `collections.deque` operations (`appendleft`, `popleft`, `rotate`, bounded `maxlen`).

### 5. Control Flow & Data Processing (`03_control_flow_and_data/`)
- [`01_control_flow.py`](03_control_flow_and_data/01_control_flow.py): `enumerate()`, generator functions (`yield`), list comprehensions.
- [`02_regex_and_json.py`](03_control_flow_and_data/02_regex_and_json.py): Regular expressions (`re`) and JSON serialization (`json`).
- [`03_csv_and_match_case.py`](03_control_flow_and_data/03_csv_and_match_case.py): Reading CSV files (`csv.DictReader`, `csv.reader`, `next()`), structural pattern matching (`match / case`).
- [`04_sqlite_basics.py`](03_control_flow_and_data/04_sqlite_basics.py): SQLite DB connectivity (`sqlite3`), querying (`WHERE`, `LIMIT`, `OFFSET`), and row retrieval (`fetchall()`, `fetchone()`, `fetchmany()`).

### 6. Functional Programming (`04_functional_programming/`)
- [`01_lambdas.py`](04_functional_programming/01_lambdas.py): Lambda syntax, default parameters, `map()`, and `filter()`.
- [`02_args_and_kwargs.py`](04_functional_programming/02_args_and_kwargs.py): Packing (`*args` tuple, `**kwargs` dict) and unpacking sequences/dictionaries into functions.

### 7. External Libraries (`05_external_libraries/`)
- [`01_faker_basics.py`](05_external_libraries/01_faker_basics.py): Mock data generation with `faker` and nested dict structures.
- [`02_csv_writing_with_faker.py`](05_external_libraries/02_csv_writing_with_faker.py): Writing CSV data with `faker` using `csv.writer` (positional rows) and `csv.DictWriter` (dictionary records).
- [`03_sqlite_faker_inserts.py`](05_external_libraries/03_sqlite_faker_inserts.py): SQLite schema initialization (`CREATE TABLE IF NOT EXISTS`), single insert (`execute`), batch insert (`executemany`), and `Faker` integration.

### 8. Interactive Projects (`projects/`)
- [`interactive_quiz.py`](projects/interactive_quiz.py): CLI multiple-choice quiz game.
- [`number_guessing.py`](projects/number_guessing.py): Configurable difficulty number guessing game.
- [`cmatrix.py`](projects/cmatrix.py): Terminal Matrix rain animation.
