"""
File I/O Operations & Path Management (pathlib.Path)

Concepts:
- Open modes: Write (`w`), Append (`a`), Read (`r`).
- Path handling using standard `pathlib.Path`.
- Safe file operations with `with` context manager.
- Reading methods (`read()`, `readline()`, `readlines()`).
"""

from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "temp_files"


def demo_file_io() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    sample_file = OUTPUT_DIR / "demo_notes.txt"

    # 1. Writing to a file (mode='w' overwrites content)
    with open(sample_file, mode="w", encoding="utf-8") as f:
        f.write("Line 1: Python File I/O Basics\n")
        f.write("Line 2: Context managers auto-close files.\n")

    print(f"1. Written file: {sample_file.name}")

    # 2. Appending to a file (mode='a')
    with open(sample_file, mode="a", encoding="utf-8") as f:
        f.write("Line 3: Appended content.\n")

    print("2. Appended content.")

    # 3. Reading file line by line (mode='r')
    print("\n3. Reading File Line by Line:")
    with open(sample_file, mode="r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            print(f"  [{line_num}] {line.strip()}")

    # 4. Reading all lines into a list
    with open(sample_file, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"\n4. Readlines list length: {len(lines)} lines")


if __name__ == "__main__":
    demo_file_io()
