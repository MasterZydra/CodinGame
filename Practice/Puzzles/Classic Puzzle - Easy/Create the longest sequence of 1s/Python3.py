import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input().split("0")

longest = 1
for i in range(len(b) - 1):
    longest = max(longest, len(b[i] + b[i + 1]) + 1)

print(longest)
