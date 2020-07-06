import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
class tree:
    def __init__(self):
        self.children = list()
        self.value = None
    
    def fillTree(self, values: str):
        self.value = values[0]
        if len(values) == 1:
            return
        
        # Search for matching child
        for child in self.children:
            if child.value == values[1]:
                child.fillTree(values[1:])
                return

        # Add new child
        subTree = tree()
        subTree.fillTree(values[1:])
        self.children.append(subTree)

    def count(self) -> int:
        # Count itself
        counter = 1
        # Count children
        for child in self.children:
            counter += child.count()
        return counter

n = int(input())
phonetree = tree()
for i in range(n):
    telephone = input()
    # Add space for tree above the number trees
    phonetree.fillTree(" " + telephone)

# The number of elements (referencing a number) stored in the structure.
# Minus one for tree above the number trees
print(phonetree.count() - 1)
