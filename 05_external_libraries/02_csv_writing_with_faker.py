"""
Writing CSV Files using csv.writer and csv.DictWriter with Faker

Concepts:
- Generating mock student records using Faker.
- Writing rows using positional tuples/lists with `csv.writer`.
- Writing header and dictionary rows with `csv.DictWriter`.
"""

import csv
from pathlib import Path
from faker import Faker

OUTPUT_DIR = Path(__file__).resolve().parent


# 1. Writing CSV using csv.writer (Positional Rows)
def write_students_with_writer() -> None:
    file_path = OUTPUT_DIR / "students_writer.csv"
    f = Faker()

    # Ordered list of column headers
    columns = ["student_id", "student_name", "course"]

    # newline="" prevents extra blank lines on Windows
    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_w = csv.writer(csv_file)

        # Write header row
        csv_w.writerow(columns)

        # Write 5 generated data rows (as tuples)
        for x in range(0, 5):
            csv_w.writerow((x + 1, f.first_name(), "BSIT"))

    print(f"Written file using csv.writer: {file_path.name}")


# 2. Writing CSV using csv.DictWriter (Dictionary Rows)
def write_students_with_dictwriter() -> None:
    file_path = OUTPUT_DIR / "students_dictwriter.csv"
    f = Faker()

    columns = ["student_id", "student_name", "course"]

    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_w = csv.DictWriter(csv_file, fieldnames=columns)

        # Write fieldnames header
        csv_w.writeheader()

        # Generate list of dictionaries using List Comprehension
        students_list = [
            {
                "student_name": f.first_name(),
                "course": "BSIT",
                "student_id": x + 1,
            }
            for x in range(0, 5)
        ]

        # Write dictionary rows
        for r in students_list:
            csv_w.writerow(r)

    print(f"Written file using csv.DictWriter: {file_path.name}")


if __name__ == "__main__":
    print("=== CSV Generation with Faker ===")
    write_students_with_writer()
    write_students_with_dictwriter()
