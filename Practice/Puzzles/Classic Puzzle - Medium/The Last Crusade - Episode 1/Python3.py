import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

grid = list()

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    grid.append([int(x) for x in line.split()])
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    xn = xi
    yn = yi
    room = grid[yi][xi]

    if (room in [1, 3, 7, 8, 9, 12, 13] or
    (room == 4 and pos == "RIGHT") or
    (room == 5 and pos == "LEFT")):
        yn += 1
    
    if (room == 10 or
    (room == 4 and pos == "TOP") or
    (room in [2, 6] and pos == "RIGHT")):
        xn -= 1

    if (room == 11 or
    (room in [2, 6] and pos == "LEFT") or
    (room == 5 and pos == "TOP")):
        xn += 1

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(str(xn) + " " + str(yn))
