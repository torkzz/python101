"""
SQLite Database Schema Creation & Data Population using Faker

Concepts:
- Creating tables conditionally (`CREATE TABLE IF NOT EXISTS`).
- Parameterized queries (`?` placeholders) to prevent SQL injection.
- Single record insertion (`cur.execute`).
- Batch record insertion with list comprehension (`cur.executemany`).
- Committing transactions (`db.commit()`).
"""

import sqlite3
from pathlib import Path
from faker import Faker

OUTPUT_DIR = Path(__file__).resolve().parent


def populate_students_db() -> None:
    db_path = OUTPUT_DIR / "student.sqlite"
    f = Faker()

    with sqlite3.connect(db_path) as db:
        cur = db.cursor()

        # 1. Create table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name VARCHAR,
                course VARCHAR
            )
        """)
        db.commit()

        # 2. Parameterized INSERT query
        insert_query = "INSERT INTO students (student_name, course) VALUES (?, ?)"

        # Single insertion via cur.execute()
        cur.execute(insert_query, (f.first_name(), "BSCpE"))

        # Batch insertion via cur.executemany() with list comprehension
        input_vals = [(f.first_name(), "BSCpE") for _ in range(0, 3)]
        cur.executemany(insert_query, input_vals)

        # Commit transaction
        db.commit()

        # 3. Query back inserted records to verify
        cur.execute("SELECT id, student_name, course FROM students ORDER BY id DESC LIMIT 4")
        records = cur.fetchall()

        print(f"Database file: {db_path.name}")
        print("Latest inserted student records:")
        for r in records:
            print(f"  ID: {r[0]} | Name: {r[1]} | Course: {r[2]}")


if __name__ == "__main__":
    print("=== SQLite Schema Creation & Faker Population ===")
    populate_students_db()
