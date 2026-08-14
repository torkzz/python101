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
8. [Object-Oriented Programming (`06_oop/`)](#8-object-oriented-programming-06_oop)
9. [Unit Testing (`07_testing/`)](#9-unit-testing-07_testing)
10. [AWS Cloud (`08_aws_cloud/`)](#10-aws-cloud-08_aws_cloud)
11. [Interactive Projects (`projects/`)](#11-interactive-projects-projects)

---

## Lesson Modules

### 2. Coding Standards & Guidelines (`00_guidelines/`)
- [`00_pep8_rules.py`](00_guidelines/00_pep8_rules.py): PEP 8 naming conventions, formatting, EAFP principles, and type annotations.
- [`01_venv_setup.py`](00_guidelines/01_venv_setup.py): Virtual environment (`venv`) creation, activation, `pip` package installation, and execution inspection.
- [`02_docstrings_and_tricks.py`](00_guidelines/02_docstrings_and_tricks.py): Docstring standards (PEP 257), variable swapping (`a, b = b, a`), extended unpacking (`*rest`), f-string debug formatting (`f"{var=}"`), parallel iteration (`zip`), and walrus assignment (`:=`).

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
- [`05_asyncio_basics.py`](03_control_flow_and_data/05_asyncio_basics.py): Asynchronous programming (`async def`, `await`, `asyncio.run()`), offloading blocking I/O to background threads using `asyncio.to_thread()`, and concurrent execution using `asyncio.gather()`.
- [`06_exceptions_handling.py`](03_control_flow_and_data/06_exceptions_handling.py): Handling errors with `try`, `except`, `else` (runs on success), `finally` (always runs), and `raise`.
- [`07_file_io_basics.py`](03_control_flow_and_data/07_file_io_basics.py): File handling (`r`, `w`, `a`), line reading (`readlines`), and modern path management with `pathlib.Path`.

### 6. Functional Programming (`04_functional_programming/`)
- [`01_lambdas.py`](04_functional_programming/01_lambdas.py): Lambda syntax, default parameters, `map()`, and `filter()`.
- [`02_args_and_kwargs.py`](04_functional_programming/02_args_and_kwargs.py): Packing (`*args` tuple, `**kwargs` dict) and unpacking sequences/dictionaries into functions.
- [`03_decorators_basics.py`](04_functional_programming/03_decorators_basics.py): Decorator pattern basics, wrapper functions (`inner_method`), decorator `@` syntax, and function behavior modification.
- [`04_decorators_with_args.py`](04_functional_programming/04_decorators_with_args.py): Decorators with function arguments, wrapper parameter interception (`multiply_values(x, y)`), definition-time execution vs call-time execution.
- [`05_logging_decorators.py`](04_functional_programming/05_logging_decorators.py): Standard `logging` module integration (`getLogger`, `basicConfig`, `l.debug`, `l.warning`, `l.error`) with custom header banner decorators (`@prepend_log`).

### 7. External Libraries (`05_external_libraries/`)
- [`01_faker_basics.py`](05_external_libraries/01_faker_basics.py): Mock data generation with `faker` and nested dict structures.
- [`02_csv_writing_with_faker.py`](05_external_libraries/02_csv_writing_with_faker.py): Writing CSV data with `faker` using `csv.writer` (positional rows) and `csv.DictWriter` (dictionary records).
- [`03_sqlite_faker_inserts.py`](05_external_libraries/03_sqlite_faker_inserts.py): SQLite schema initialization (`CREATE TABLE IF NOT EXISTS`), single insert (`execute`), batch insert (`executemany`), and `Faker` integration.
- [`04_requests_http_basics.py`](05_external_libraries/04_requests_http_basics.py): Making HTTP GET and POST requests using `requests`, passing custom headers, JSON body payload, and parsing JSON response outputs.
- [`05_api_deck_of_cards.py`](05_external_libraries/05_api_deck_of_cards.py): Working with external REST APIs (Deck of Cards API), extracting dynamic parameters (`deck_id`), and iterating over cards collections.
- [`06_aiohttp_async_requests.py`](05_external_libraries/06_aiohttp_async_requests.py): Native asynchronous HTTP requests with `aiohttp`, managing session lifecycles (`async with aiohttp.ClientSession()`), non-blocking response reading (`await r.text()`), and multi-URL concurrency (`asyncio.gather()`).
- [`07_web_scraping_bs4.py`](05_external_libraries/07_web_scraping_bs4.py): HTML DOM parsing with `BeautifulSoup4`, finding elements (`find`, `find_all`), and text extraction (`get_text().strip()`).

### 8. Object-Oriented Programming (`06_oop/`)
- [`01_mro_and_inheritance.py`](06_oop/01_mro_and_inheritance.py): Multiple inheritance, Method Resolution Order (MRO), `super()` resolution, and MRO chain inspection using `.mro()`.
- [`02_abstract_classes.py`](06_oop/02_abstract_classes.py): Abstract Base Classes (`from abc import ABC, abstractmethod`), enforcing interface contracts, `@abstractmethod` decorator, and concrete class inheritance.
- [`03_properties_and_encapsulation.py`](06_oop/03_properties_and_encapsulation.py): Protected attributes (`_attr`), private mangling (`__attr`), property getters/setters (`@property`, `@setter`), and utility methods (`@staticmethod`).

### 9. Unit Testing (`07_testing/`)
- [`01_unittest_basics.py`](07_testing/01_unittest_basics.py): Standard `unittest` framework, inheriting from `unittest.TestCase`, test assertions (`assertEqual`, `assertNotEqual`), custom failure messages, and `unittest.main()` execution.
- [`02_unittest_assertions.py`](07_testing/02_unittest_assertions.py): Cheat sheet for `unittest.TestCase` assertions (`assertEqual`, `assertNotEqual`, `assertTrue`, `assertFalse`, `assertIs`, `assertIsNot`, `assertIsNone`, `assertIsNotNone`, `assertIn`, `assertNotIn`, `assertIsInstance`, `assertRaises`), plus `assertEqual` vs `assertIs` (value equality vs object identity).

### 10. AWS Cloud (`08_aws_cloud/`)
- [`01_lambda_handler_basics.py`](08_aws_cloud/01_lambda_handler_basics.py): Basic structure of AWS Lambda Python functions (`def lambda_handler(event, context)`), logging initialization (`getLogger()`, `setLevel("INFO")`), AWS SDK integration (`boto3`, `botocore.config.Config`), parsing event parameters, and returning API Gateway HTTP JSON responses (`statusCode`, `headers`, `body`).

### 11. Interactive Projects (`projects/`)
- [`interactive_quiz.py`](projects/interactive_quiz.py): CLI multiple-choice quiz game.
- [`number_guessing.py`](projects/number_guessing.py): Configurable difficulty number guessing game.
- [`cmatrix.py`](projects/cmatrix.py): Terminal Matrix rain animation.
- [`blackjack.py`](projects/blackjack.py): Beginner CLI Blackjack card game using `requests` and Deck of Cards API with full dealer logic.
