import sys
import math

# Don't let the machines win. You are humanity's last hope...

grid = []

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    grid.append(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0

for i in range(len(grid)): # y
    y1 = i
    for c in range(len(grid[i])): #x
        if grid[i][c] == '.':
            continue    
        x1 = c
        x2 = -1
        y2 = -1
        x3 = -1
        y3 = -1
        
        for n in range(c +1, len(grid[i])):

            if grid[i][n] == '.':
                continue
        
            if (n) < len(grid[i]) and grid[i][n] == '0':
                x2 = n
                y2 = i
                break
        
        for u in range(i + 1, len(grid)):
            if (u) < len(grid) and grid[u][c] == '0':
                x3 = c
                y3 = u
                break
# Three coordinates: a node, its right neighbor, its bottom neighbor
        print('{} {} {} {} {} {}'.format(x1, y1, x2, y2, x3, y3))