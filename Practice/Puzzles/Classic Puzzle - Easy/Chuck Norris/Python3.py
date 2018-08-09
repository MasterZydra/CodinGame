import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(7)[::-1])

###### Chars to int
intMessage = ''
for c in message:
    intMessage += str(ord(c)) + ','

###### Ints to bin
binMessage = ''
i = 0
ch = intMessage.split(',')
for c in ch:
    if c != '':
        #print >> sys.stderr, str(int(c))
        binMessage += str(toBinary(int(float(c))))

#print >> sys.stderr, binMessage

##### Bin to output
outMessage = ''
i = 0
l = len(binMessage)
while i < l:
    s = binMessage[i]
    j = i+1
    count = 1
    while j < l:
        if binMessage[j] == s: 
            j += 1
            count += 1
        else: break;
    
    i = j
    if s == '1': outMessage += '0 '
    if s == '0': outMessage += '00 '
    
    k = 0
    while k < count: outMessage += '0'; k+=1
    
    if i < len(binMessage): outMessage += ' '

print(outMessage)