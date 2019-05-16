import sys
import math

def lineCol(colIndex):
    return (colIndex - 1) * 3

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
w, h = [int(i) for i in input().split()]

# Get number of vertical lines from given width
nCol = int((w - 4)/3 + 2)
# Contains end line for each vertical line
lines = [*range(1, nCol + 1)]
# Contains vertical line name
chars = input().split()

for i in range(h - 2):
    line = input()
    if not "-" in line: continue
    for j in range(0, nCol):
        b = lineCol(lines[j]) - 1
        a = lineCol(lines[j]) + 1
        if b > 0:
            if line[b] == "-":
                lines[j] -= 1
        if a >= 0 and len(line) - 1 >= a:
            if line[a] == "-":
                lines[j] += 1
# Contains end number of a vertical line
nums = input().split()    

# Write an action using print
for i in range(0, nCol):
    print(chars[i] + str(nums[lines[i] - 1]))
