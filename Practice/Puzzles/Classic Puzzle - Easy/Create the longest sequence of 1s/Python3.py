import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()

blocks = b.split("0")

longest = 1
for i in range(len(blocks) - 1):
    longest = max(longest, len(blocks[i] + "1" + blocks[i + 1]))

print(longest)
