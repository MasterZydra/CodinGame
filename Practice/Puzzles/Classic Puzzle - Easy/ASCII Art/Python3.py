import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    t = t.upper()
    outp = ""
    for subt in t:
        i = 0
        while i < l:
            ordn = ord(subt)
            if ordn > 91 or ordn < 65: ordn = 91
            n = (ordn-65)*l
            
            outp += row[n+i]
            i += 1
    print(outp)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
