"""
SQLite Database Queries in Python (sqlite3)

Concepts:
- Context manager database connection (`sqlite3.connect`).
- Cursor execution (`cur.execute`).
- Query results retrieval (`fetchall()`, `fetchone()`, `fetchmany()`).
- SQL clauses: `WHERE`, `LIMIT`, `OFFSET`.
"""

import sqlite3

def setup_mock_tweets_db(db_conn: sqlite3.Connection) -> None:
    """Create in-memory table and seed sample tweets."""
    cur = db_conn.cursor()
    cur.execute("""
        CREATE TABLE Tweets (
            id INTEGER PRIMARY KEY,
            airline TEXT,
            airline_sentiment TEXT,
            negativereason TEXT,
            text TEXT
        )
    """)

    sample_tweets = [
        ("AirExpress", "negative", "Late Flight", "Flight delayed by 2 hours."),
        ("AirExpress", "positive", "", "Great customer service!"),
        ("SkyLine", "negative", "Cancelled Flight", "My flight was cancelled without notice."),
        ("SkyLine", "neutral", "", "Flight arrived on schedule."),
        ("AirExpress", "negative", "Lost Luggage", "Luggage missing on arrival."),
    ]

    cur.executemany("""
        INSERT INTO Tweets (airline, airline_sentiment, negativereason, text)
        VALUES (?, ?, ?, ?)
    """, sample_tweets)
    db_conn.commit()


def run_sqlite_demo() -> None:
    # Use in-memory database for self-contained, instant execution
    with sqlite3.connect(":memory:") as db:
        setup_mock_tweets_db(db)

        cur = db.cursor()

        # Query with WHERE, LIMIT, and OFFSET
        rs = cur.execute("""
            SELECT airline, negativereason, text 
            FROM Tweets 
            WHERE airline_sentiment = 'negative' 
            LIMIT 10 OFFSET 0
        """)

        # Fetch methods overview:
        # - cur.fetchone(): Fetches 1 row at a time.
        # - cur.fetchmany(size): Fetches a specific chunk of rows.
        # - cur.fetchall(): Fetches all remaining matching rows as a list of tuples.

        rows = rs.fetchall()
        print(f"Fetched {len(rows)} negative tweet record(s):\n")

        for r in rows:
            print("Airline: {}, Reason: {}\r\n{}\n".format(r[0], r[1], r[2]))


if __name__ == "__main__":
    print("=== SQLite Database Query Demo ===")
    run_sqlite_demo()
