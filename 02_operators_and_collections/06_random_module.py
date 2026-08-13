# Standard `random` Module

import random

# 1. Random integers & choices
print("Random integer (1-10):", random.randint(1, 10))

items = ["Python", "Java", "C++", "Rust"]
print("Random choice:", random.choice(items))

# 2. In-place list shuffling
cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print("Shuffled cards:", cards)

# 3. Simple Dice Roller Example
dice = random.randint(1, 6)
print(f"\nDice Roll: {dice}")
