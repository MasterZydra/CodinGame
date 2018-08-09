import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
minX=minY=0
maxX=w
maxY = h
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if "U" in bomb_dir:
        maxY = y0-1
    
    if "D" in bomb_dir:
        minY = y0+1
    
    if "L" in bomb_dir:
        maxX = x0-1
    
    if "R" in bomb_dir:
        minX = x0+1
    
    #Find middle
    x0 = (minX + maxX)/2
    y0 = (minY + maxY)/2
    
    # the location of the next window Batman should jump to.
    print(str(int(x0)) + " " + str(int(y0)))
   