import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

summe = 0
count = 0
budgets=[]
n = int(input())
c = int(input())
for i in range(n):
    b = int(input())
    budgets.append(b)
    summe += b
c2 = c
r = 0
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
budgets.sort()

if summe >= c:
    # Logik - Teil
    i = n
    for budget in budgets:
        # Wenn budget kleiner seinem Anteil
        if c/(n-count) >= budget:
            print(budget)
            c-=int(budget)
            c2-=int(budget)
            count+=1
            i-=1
            continue
        
        # Wenn budget groesser gleich Anteil, mach es
        if c/(n-count) < budget:
            r=c - int(c/(n-count)) * (n-count)
            
            if i <= r:
                print(int(c/(n-count)+1))
                c2 -= int(c/(n-count)+1)
                i-=1
                continue
            
            print(int(c/(n-count)))
            c2 -= int(c/(n-count))
            i-=1
            continue
else:print("IMPOSSIBLE")