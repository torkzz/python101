"""
Virtual Environment (venv) Setup & Package Management Guide

This module demonstrates how virtual environments isolate dependencies
and prevent pollution of system-wide Python installations.

CLI Execution Flow:
-------------------
1. Creation:
   python3 -m venv .venv

2. Activation:
   - Linux/macOS (Bash/Zsh):
     source .venv/bin/activate
   - Windows (Command Prompt):
     .venv\\Scripts\\activate.bat
   - Windows (PowerShell):
     .venv\\Scripts\\Activate.ps1

3. Package Management & Requirements:
   pip install --upgrade pip
   pip install faker
   pip freeze > requirements.txt
   pip install -r requirements.txt

4. Deactivation:
   deactivate
"""

import sys
from pathlib import Path


def check_active_environment() -> None:
    """Detect if script is running inside a Virtual Environment."""
    in_venv = sys.prefix != sys.base_prefix

    print("=== Python Environment Status Inspector ===")
    print(f"Python Executable : {sys.executable}")
    print(f"System Base Prefix: {sys.base_prefix}")
    print(f"Active Env Prefix : {sys.prefix}")

    if in_venv:
        print("\nStatus: Running inside a Virtual Environment (.venv)")
    else:
        print("\nStatus: Running on System Python (Global Environment)")


def check_requirements_file() -> None:
    """Inspect requirements.txt file in project root."""
    req_path = Path(__file__).resolve().parent.parent / "requirements.txt"

    print("\n=== Requirements Setup Inspector ===")
    if req_path.exists():
        print(f"Found requirements.txt at: {req_path}")
        content = req_path.read_text(encoding="utf-8").strip()
        print("Configured Dependencies:")
        for line in content.splitlines():
            print(f"  - {line}")
    else:
        print(f"requirements.txt missing at {req_path}")


if __name__ == "__main__":
    check_active_environment()
    check_requirements_file()
