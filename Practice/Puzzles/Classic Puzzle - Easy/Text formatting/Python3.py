def replace(old, new, str):
    while old in str:
        str = str.replace(old, new)
    return str

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
intext = input()

# Remove spaces before punctuation marks
intext = replace(" ,", ", ", intext)
intext = replace(" .", ". ", intext)

# Remove duplicate punctuation marks
intext = replace("..", ".", intext)
intext = replace(",,", ",", intext)

# Space after each punctuation mark
intext = intext.replace(",", ", ")
intext = intext.replace(".", ". ")

# Remove space at start and end of string
intext = intext.strip()

# Remove multiple spaces
intext = replace("  ", " ", intext)

# Text to lower
intext = intext.lower()

# First char to upper
intext = intext[0].upper() + intext[1:]

# First char after dot to upper
pos = 0
found = True
while found:
    beginSent = intext.find(". ", pos)
    if beginSent == -1:
        found = False
        continue
    pos = beginSent + 2
    if pos < len(intext):
        intext = intext[0:pos] + intext[pos].upper() + intext[pos+1:]


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(intext)
