# Interactive Fundamentals Quiz App

import random

QUESTIONS = [
    {
        "prompt": "What is the return type of 10 // 3 in Python?",
        "options": ["a) float", "b) int", "c) str", "d) list"],
        "answer": "b"
    },
    {
        "prompt": "Which collection type guarantees unique elements?",
        "options": ["a) list", "b) tuple", "c) set", "d) dict"],
        "answer": "c"
    },
    {
        "prompt": "What method safely fetches a dict value without raising KeyError?",
        "options": ["a) fetch()", "b) get()", "c) pop()", "d) extract()"],
        "answer": "b"
    },
    {
        "prompt": "Which keyword turns a regular function into a generator?",
        "options": ["a) return", "b) yield", "c) generate", "d) async"],
        "answer": "b"
    }
]

def run_quiz():
    print("=== Python Fundamentals Quiz ===")
    score = 0
    shuffled = QUESTIONS.copy()
    random.shuffle(shuffled)

    for idx, q in enumerate(shuffled, start=1):
        print(f"\nQ{idx}: {q['prompt']}")
        for opt in q["options"]:
            print(f"   {opt}")

        user_ans = input("Your answer (a/b/c/d): ").strip().lower()
        if user_ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was: {q['answer']}")

    print(f"\nFinal Score: {score}/{len(QUESTIONS)} ({score / len(QUESTIONS) * 100:.0f}%)")

if __name__ == "__main__":
    run_quiz()
