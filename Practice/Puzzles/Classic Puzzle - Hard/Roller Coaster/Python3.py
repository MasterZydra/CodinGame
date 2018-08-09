import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

earnings = 0
groups = []
cacheEarning = dict()
cacheIndex = dict()
index = int(0)

l, c, n = [int(i) for i in input().split()]
for i in range(n):
    pi = int(input())
    groups.append(pi)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in range(c):
    placeCount = 0
    beginIndex = index
    beginIndexB = False
    
    while placeCount <= l:
        
        if beginIndex in cacheEarning:
            earnings += cacheEarning[beginIndex]
            index = cacheIndex[beginIndex]
            break
        
        if beginIndex == index:
            if beginIndexB: break
            if not beginIndexB: beginIndexB = True
        if placeCount + groups[index] <= l:
            placeCount += groups[index]
            
            if index + 1 < len(groups): index += 1
            else: index = 0
        else: break
    
    earnings += placeCount
    
    if not beginIndex in cacheEarning:
        cacheEarning[beginIndex] = placeCount
        cacheIndex[beginIndex] = index

print(earnings)
