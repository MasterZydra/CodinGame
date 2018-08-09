import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def CheckWord(word, letters):
    for l in word:
        if word.count(l) > letters.count(l): return -1
    return 1

def ProcWord(word, letters):
    c1  = word.count('e')
    c1 += word.count('a')
    c1 += word.count('i')
    c1 += word.count('o')
    c1 += word.count('n')
    c1 += word.count('r')
    c1 += word.count('t')
    c1 += word.count('l')
    c1 += word.count('s')
    c1 += word.count('u')
    
    c2  = word.count('d')
    c2 += word.count('g')
    c2 *= 2
    
    c3  = word.count('b')
    c3 += word.count('c')
    c3 += word.count('m')
    c3 += word.count('p')
    c3 *= 3
    
    c4  = word.count('f')
    c4 += word.count('h')
    c4 += word.count('v')
    c4 += word.count('w')
    c4 += word.count('y')
    c4 *= 4
    
    c5  = word.count('k') * 5

    c8  = word.count('j')
    c8 += word.count('x')
    c8 *= 8

    c10  = word.count('q')
    c10 += word.count('z')
    c10 *= 10
    
    return c1 + c2 + c3 + c4 + c5 + c8 + c10

listWords = list()
n = int(input())
for i in range(n):
    listWords.append(input())
    
listLetters = input()

maxWord = 0
Word = ""

for w in listWords:
    if CheckWord(w, listLetters) == 1:
        wP = ProcWord(w, listLetters) 
        if (wP > maxWord):
            maxWord = wP
            Word = w
    else: continue

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(Word)