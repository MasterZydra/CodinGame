import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

exts = []
mts = []

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    exts.append(ext.lower())
    mts.append(mt)
for i in range(q):
    fname = input()  # One file name per line.
    fn = fname.split('.')
    
    try:
        if len(fn) > 1:
            print(mts[exts.index(str(fn[len(fn)-1]).lower())])
        else:    
            print('UNKNOWN')
    except ValueError:
        print('UNKNOWN')