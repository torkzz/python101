# Challenge 1 - Number Guessing Game
# =========================================================
#
# Objective:
# Create a Python Number Guessing Game where
# the player attempts to guess a randomly
# generated number.
#
# ---------------------------------------------------------
# Instructions:
#
# Develop a program that:
#
# ✔ generates a random number
# ✔ asks the user to guess the number
# ✔ checks if the guess is correct
# ✔ gives hints to the player
# ✔ continues until the correct number is guessed
#
# ---------------------------------------------------------
# Required Features:
#
# 1. Import the random module
#
# 2. Generate a random number
#    Example:
#
#       random.randint(1, 100)
#
# 3. Ask the player to enter a guess
#
# 4. Compare the guess with the secret number
#
# 5. Display hints such as:
#
#    ✔ Too high!
#    ✔ Too low!
#    ✔ Correct!
#
# 6. Repeat the game using loops until
#    the player guesses correctly
#
# ---------------------------------------------------------
# Sample Output:
#
# Guess the number between 1 and 100
#
# Enter your guess: 50
# Too low!
#
# Enter your guess: 75
# Too high!
#
# Enter your guess: 63
# Correct! You guessed the number.
#
# ---------------------------------------------------------
# Advanced Challenges (Optional):
#
# ✔ Count the number of attempts
# ✔ Add difficulty levels
# ✔ Limit the number of tries
# ✔ Add score tracking
# ✔ Allow replay after winning
#
# ---------------------------------------------------------
# Suggested Features:
#
# Difficulty Levels:
#
# Easy   : 1 - 10
# Medium : 1 - 50
# Hard   : 1 - 100
#
# ---------------------------------------------------------
# Bonus Challenge:
#
# Create a multiplayer version where:
#
# ✔ Player 1 sets the secret number
# ✔ Player 2 tries to guess it
#

import random as r

print("="*10+"number guessting"+"="*10)
print("1-easy   (1 - 10) attempts: 8")
print("2-medium (1 - 50) attempts: 5")
print("3-hard   (1 - 100 attempts: 5)")
print("4-hardest   (1 - 1000 attempts: 1)")

difficulty = input("difficulty: ")
if difficulty == "1":
    secret_number = r.randint(1, 10)
    max_number = 10
    max_attempts = 8

elif difficulty == "2":
    secret_number = r.randint(1, 50)
    max_number = 50
    max_attempts = 5

elif difficulty == "3":
    secret_number = r.randint(1, 100)
    max_number = 100
    max_attempts = 5
elif difficulty == "4":
    # secret_number = r.randint(1, 1000)
    secret_number = 50
    max_number = 1000
    max_attempts = 1

else:
    print("error: invalid difficulty!")
    exit()

print(f"--"*5+"guess the number between 1 and {max_number}"+"--"*5)

attempts = 0
while True:
    guess = int(input("guess: "))
    attempts += 1

    if guess < secret_number:
        print("too low!")
    elif guess > secret_number:
        print("too high!")
    else:
        print("YOU WIN!")
        exit()

    print("--"*5+f"left attempts : {max_attempts-attempts}"+"--"*5)

    if  attempts >= max_attempts:
        print("*****"*5+"GAME OVER"+"*****"*5)
        exit()
