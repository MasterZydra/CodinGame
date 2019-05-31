import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

invalidISBN = []

n = int(input())
for i in range(n):
    isbn = input()
    
    if len(isbn) == 10:
        sum = 0
        try:
            for i in range(9):
                sum += (10 - i) * int(isbn[i])
        except:
            invalidISBN.append(isbn)
            continue
        
        modulo = sum % 11
        if modulo != 0:
            checkDigit = 11 - modulo
        else:
            checkDigit = 0
    
        try:
            if ((checkDigit == 10 and isbn[9] != 'X') or
                (checkDigit != 10 and int(isbn[9]) != checkDigit)):
                invalidISBN.append(isbn)
        except:
            invalidISBN.append(isbn)
            continue

    elif len(isbn) == 13:
        sum = 0
        try:
            for i in range(12):
                if i%2 == 0:
                    w = 1
                else:
                    w = 3
                sum += w * int(isbn[i])
                w -= 1
        except:
            invalidISBN.append(isbn)
            continue

        modulo = sum % 10
        if modulo != 0:
            checkDigit = 10 - modulo
        else:
            checkDigit = 0
        
        try:
            if not int(isbn[12]) == checkDigit:
                invalidISBN.append(isbn);
        except:
            invalidISBN.append(isbn)
            continue
    
    else:
        invalidISBN.append(isbn)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(str(len(invalidISBN)) + " invalid:")
for s in invalidISBN:
    print(s)
