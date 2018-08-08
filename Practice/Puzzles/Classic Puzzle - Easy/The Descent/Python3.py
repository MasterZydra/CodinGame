import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# game loop
while True:
    hiMoI = 0
    hiMo = 0
    for i in range(8):
        # represents the height of one mountain, from 9 to 0.
        mountain_h = int(input())  
        if hiMo < mountain_h: hiMo = mountain_h; hiMoI = i
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # The number of the mountain to fire on.
    print(hiMoI)