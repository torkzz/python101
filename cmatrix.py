import random
import time
import shutil
import sys

def is_allowed(char, number):
    # Printable
    if not char.isprintable():
        return False

    # Exclude common emoji / symbol ranges
    emoji_ranges = [
        (0x1F300, 0x1FAFF),  # Misc emoji
        (0x1F1E6, 0x1F1FF),  # Flags
        (0x2600, 0x27BF),    # Misc symbols / dingbats
    ]

    return not any(start <= number <= end for start, end in emoji_ranges)


# Generate Unicode pool ONCE
chars = [
    char
    for number in range(1, 55295)
    if (char := chr(number)) and is_allowed(char, number)
]

width, height = shutil.get_terminal_size()

# Generate rain ONCE
rain = []

for x in range(width):
    rain.append({
        "x": x,
        "y": random.randint(-height, 0),
        "char": random.choice(chars)
    })

GREEN = "\033[92m"
RESET = "\033[0m"

try:
    while True:

        for drop in rain:
            x = drop["x"]
            y = drop["y"]

            if 0 <= y < height:
                sys.stdout.write(
                    f"{GREEN}\033[{y + 1};{x + 1}H{drop['char']}{RESET}"
                )

            drop["y"] += 1

            if drop["y"] > height:
                drop["y"] = random.randint(-20, 0)

        sys.stdout.flush()
        time.sleep(0.05)

except KeyboardInterrupt:
    sys.stdout.write(RESET)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
