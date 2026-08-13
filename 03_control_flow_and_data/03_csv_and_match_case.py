"""
CSV Processing & Structural Pattern Matching (match / case)

Concepts:
- Standard `csv` module (`csv.reader` vs `csv.DictReader`).
- Skipping rows with `next()`.
- Chained variable initialization (`a = b = c = 0`).
- Python 3.10+ Structural Pattern Matching (`match / case`).
"""

import csv
import io

# Mock CSV dataset (simulating Tweets.csv)
SAMPLE_CSV = """tweet_id,airline_sentiment,text
1,positive,Great flight with awesome service!
2,negative,Flight was delayed 3 hours.
3,neutral,Flight departed on time.
4,negative,Lost my baggage.
5,positive,Smooth landing and friendly crew.
"""

def analyze_sentiments_dictreader(csv_data: str) -> None:
    """Read CSV as dictionaries and match by column header."""
    file_like = io.StringIO(csv_data.strip())
    reader = csv.DictReader(file_like)

    # Chained variable assignment
    neutral_sentiment = positive_sentiment = negative_sentiment = 0

    for row in reader:
        # Pattern Matching (Python 3.10+)
        match row["airline_sentiment"].lower():
            case "positive":
                positive_sentiment += 1
            case "negative":
                negative_sentiment += 1
            case "neutral":
                neutral_sentiment += 1
            case _:
                pass

    print("=== DictReader + match/case Results ===")
    print("Positive sentiments:", positive_sentiment)
    print("Negative sentiments:", negative_sentiment)
    print("Neutral sentiments:", neutral_sentiment)


def analyze_sentiments_reader(csv_data: str) -> None:
    """Read CSV as raw list rows and skip header with next()."""
    file_like = io.StringIO(csv_data.strip())
    reader = csv.reader(file_like)

    # Skip header row
    header = next(reader)
    print(f"\nSkipped Header: {header}")

    positive = negative = neutral = 0

    for row in reader:
        # Index 1 = airline_sentiment column
        match row[1].lower():
            case "positive":
                positive += 1
            case "negative":
                negative += 1
            case "neutral":
                neutral += 1

    print("=== csv.reader Results ===")
    print(f"Positive: {positive} | Negative: {negative} | Neutral: {neutral}")


if __name__ == "__main__":
    analyze_sentiments_dictreader(SAMPLE_CSV)
    analyze_sentiments_reader(SAMPLE_CSV)
