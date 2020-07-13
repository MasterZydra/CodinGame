import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def recursiveEncode(binaryMessage: str, prevResult = '') -> str:    
    result = prevResult
    count = 0
    for char in binaryMessage:
        if char != binaryMessage[0]:
            break
        count += 1
    
    result += '0 ' if binaryMessage[0] == '1' else '00 '
    result += '0' * count

    if count == len(binaryMessage):
        return result
    return recursiveEncode(binaryMessage[count:], result + ' ')

message = ''
for char in input():
    # Get ASCII value for char and use string format to get 7-digit binary
    message += "{:07b}".format(ord(char))

# Encode binary
print(recursiveEncode(message))
