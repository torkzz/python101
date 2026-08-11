import random as r

# 1. randint(start, end)
# random_num = r.randint(1, 10)
# r.seed(1)
# # print("Random number:", random_num)
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# print(r.randint(1, 10))
# # # print (r.random())
# items = ["Python", "Java", "Php", "C#", "C++", "R"]

# selected_item = r.choice(items)
# print(selected_item)

# item_1 = "I LOVE PROGRAMMING!"

# selected_item1 = r.choice(item_1)
# print(selected_item1)

# numbers = (10, 20, 30, 40, 50)

# print(r.choice(numbers))


# random_key = r.choice(list(student.values()))

# print(random_key)

# shuffle()
# changes the original list -- IN-PLACE MODIFICATION
# student = {
#     "name": "Kevin Paul",
#     "course": "MSIT",
#     "language": "C"
# }

# random_key = r.choice(list(student.values()))
# print("4. Shuffle List")

# cards = ['A', 'K', 'Q', 'J']

# print("Before Shuffle:", cards)

# shuffle1 = list(student.items())
# r.shuffle(shuffle1)

# print("After Shuffle:", shuffle1)

# print()
# range()
# randrange(start, stop, step)

# print(r.randrange(0, 20, 2))
print("=== Dice Roller Simulator ===")

# Variable to control the loop
play_again = "yes"

# Repeat while the user wants to continue
while play_again.lower() == "yes":

    print("\nRolling the dice...")

    # Generate a random number from 1 to 6
    dice = r.randint(1, 6)

    print("You rolled:", dice)

    # Simple dice face interpretation
    if dice == 1:
        print("⚀ One")
    elif dice == 2:
        print("⚁ Two")
    elif dice == 3:
        print("⚂ Three")
    elif dice == 4:
        print("⚃ Four")
    elif dice == 5:
        print("⚄ Five")
    else:
        print("⚅ Six")

    # Ask the user if they want to continue
    play_again = input("\nRoll again? (yes/no): ")

print("\nThanks for playing!")
print("Program ended.")
