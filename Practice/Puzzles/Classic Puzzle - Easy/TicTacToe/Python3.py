import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

board = list()
for i in range(3):
    line = list(input())
    board.append(line)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

winPos = -1

def checkChars(line: list) -> bool:
    global winPos
    os = 0
    dots = 0
    dotPos = 0
    for i in range(3):
        if line[i] == 'O':
            os += 1
        elif line[i] == '.':
            dots += 1
            dotPos = i

    if os == 2 and dots == 1:
        winPos = dotPos
        return True

    return False

for i in range(3):
    # Rows
    if checkChars(board[i]):
        board[i][winPos] = 'O'
        break

    # Cols
    if checkChars(board[0][i] + board[1][i] + board[2][i]):
        board[winPos][i] = 'O'
        break

# Dias
if checkChars(board[2][0] + board[1][1] + board[0][2]):
    board[2-winPos][winPos] = 'O'
elif checkChars(board[0][0] + board[1][1] + board[2][2]):
    board[winPos][winPos] = 'O'

if winPos == -1:
    print("false")
else:
    for line in board:
        print(''.join(line))
