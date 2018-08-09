import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
div = 0
maxValue = 0
n = int(input())
for i in input().split():
    if n == 0: maxValue = i
    
    maxValue = max(int(i), int(maxValue))
    div = max(int(maxValue) - int(i), int(div))
    
print(div * -1)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)