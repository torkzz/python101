# Double-Ended Queue: collections.deque

"""
deque (Double-Ended Queue) provides O(1) time complexity for appends
and pops from both sides, compared to list O(n) for left-side operations.
"""

from collections import deque

# 1. Initialization
dq = deque([10, 20, 30])
print("Initial deque:", dq)

# 2. Fast O(1) operations on both ends
dq.append(40)        # Append to right
dq.appendleft(0)     # Append to left
print("\nAfter append & appendleft:", dq)

right_val = dq.pop()        # Remove from right -> 40
left_val = dq.popleft()     # Remove from left  -> 0
print(f"Popped right: {right_val}, Popped left: {left_val}")
print("Remaining deque:", dq)

# 3. Rotating elements
# Positive n rotates right, negative n rotates left
dq.rotate(1)
print("\nRotated 1 step right:", dq)

dq.rotate(-1)
print("Rotated 1 step left:", dq)

# 4. Bounded deque (max length enforces sliding window)
history = deque(maxlen=3)
for i in range(1, 6):
    history.append(f"Event_{i}")
    print(f"Added Event_{i} -> History (maxlen=3): {list(history)}")
