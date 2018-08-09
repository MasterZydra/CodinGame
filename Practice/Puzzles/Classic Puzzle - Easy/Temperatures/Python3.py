import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

tempArr = temps.split(' ')
lowestNum = 5526

try:
    for temp in tempArr:
        if (abs(float(temp)) < abs(lowestNum) or
        (abs(float(temp)) == abs(lowestNum)) and (float(temp) > lowestNum)):
            lowestNum = int(float(temp))
            
    print(lowestNum)
except:
    print(0)