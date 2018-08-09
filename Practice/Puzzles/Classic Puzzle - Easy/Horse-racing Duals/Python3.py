import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
horses = []
n = int(input())
for i in range(n):
    pi = int(input())
    horses.append(pi)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

horses.sort()
smDiv = 10000000

i = 0
while i < n-1:
    hDiv = horses[i+1] - horses[i]
    smDiv = min(hDiv, smDiv)
    i+=1

print(smDiv)