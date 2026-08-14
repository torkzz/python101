"""
Logging Module & Decorator Integration

Concepts:
- Standard `logging` module (`getLogger()`, `basicConfig()`, logging levels).
- Combining custom decorators with logging (`l.debug`, `l.warning`, `l.error`).
- String repetition multiplier (`"*****" * 10`).
- Decorating logging functions to prepend banner metadata.
"""

import logging
from typing import Callable

# Configure root logger with DEBUG level
l = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


def prepend_log(func: Callable[[str], None]) -> Callable[[str], None]:
    """Decorator that prepends logging banners around function execution."""
    def write_log_info(appname: str) -> None:
        l.debug("*****" * 10)
        l.debug("Starting to log {}".format(appname))
        l.debug("*****" * 10)

        return func(appname)

    return write_log_info


@prepend_log
def write_log(appname: str) -> None:
    l.warning("App {} has thrown a log warning".format(appname))


@prepend_log
def write_error(appname: str) -> None:
    l.error("App {} returned an error!".format(appname))


def main() -> None:
    write_log("My Awesome App")
    write_error("Another app")


if __name__ == "__main__":
    main()
