import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = [input()]
l = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(l-1):
    temp = list()
    lastChar = r[0]
    counter = 0
    for char in r:
        if lastChar == char:
            counter += 1
        else:
            temp.extend([str(counter), lastChar])
            lastChar = char
            counter = 1

    temp.extend([str(counter), lastChar])

    r = temp
    
print(" ".join(r))
