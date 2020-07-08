import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

board = list()
for i in range(3):
    line = input()
    board.append(line)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

winPos = -1

def checkChars(line: str) -> bool:
    global winPos
    os = 0
    dots = 0
    for char in line:
        if char == 'O':
            os += 1
        elif char == '.':
            dots += 1

    if os == 2 and dots == 1:
        winPos = line.find('.')
        return True

    return False

for i in range(3):
    # Rows
    if checkChars(board[i]):
        board[i] = 'OOO'
        break

    # Cols
    line = board[0][i] + board[1][i] + board[2][i]
    if checkChars(line):
        newLine = ''
        if i > 0:
            newLine += board[winPos][0:i]
        newLine += 'O' + board[winPos][i+1::]
        board[winPos] = newLine
        break

# Dias
linePos = board[2][0] + board[1][1] + board[0][2]
if checkChars(linePos):
    newLine = ''
    if winPos > 0:
        newLine += board[2-winPos][0:winPos]
    newLine += 'O' + board[2-winPos][winPos + 1::]
    board[2-winPos] = newLine

lineNeg = board[0][0] + board[1][1] + board[2][2]
if checkChars(lineNeg):
    newLine = ''
    if winPos > 0:
        newLine += board[winPos][0:winPos]
    newLine += 'O' + board[winPos][winPos + 1::]
    board[winPos] = newLine

if winPos == -1:
    print("false")
else:
    for line in board:
        print(line)
