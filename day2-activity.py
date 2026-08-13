# Challenge: Number Guessing Game

import random

def play_game():
    difficulties = {
        "1": ("Easy (1-10)", 10, 8),
        "2": ("Medium (1-50)", 50, 5),
        "3": ("Hard (1-100)", 100, 5)
    }

    print("=== Number Guessing Game ===")
    for key, (label, _, attempts) in difficulties.items():
        print(f"{key}. {label} | Attempts: {attempts}")

    choice = input("Select difficulty (1-3): ").strip()
    if choice not in difficulties:
        print("Invalid choice!")
        return

    _, max_num, max_attempts = difficulties[choice]
    secret = random.randint(1, max_num)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_num}:")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"YOU WIN! Guessed in {attempts} attempt(s).")
            return

        print(f"Attempts remaining: {max_attempts - attempts}\n")

    print(f"GAME OVER! The secret number was {secret}.")

if __name__ == "__main__":
    play_game()
