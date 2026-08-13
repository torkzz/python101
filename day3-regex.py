# Regular Expressions (re) & JSON Handling

import re
import json

text = """
Name: Kevin Paul
Contact: 0917-123-4567
Email: kevin@example.com
"""

# 1. Regex searching & matching
phone_pattern = r"\d{4}-\d{3}-\d{4}"
email_pattern = r"\S+@\S+"

phones = re.findall(phone_pattern, text)
emails = re.findall(email_pattern, text)

print("Phones found:", phones)
print("Emails found:", emails)

# 2. JSON Serialization & Deserialization
student = {"name": "Kevin", "message": "こんにちは", "emoji": "🔥"}

# Convert Python dict to JSON string
json_str = json.dumps(student, ensure_ascii=False)
print("\nJSON String:", json_str)

# Parse JSON string back to Python dict
parsed = json.loads(json_str)
print("Parsed Name:", parsed["name"])
