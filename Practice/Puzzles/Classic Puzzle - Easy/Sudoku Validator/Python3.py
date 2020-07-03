import sys
import math

class Sudoku:
  def __init__(self):
    self.lines = []

  def assign(self, src):
    self.lines = src

  def getRow(self, rowIndex):
    return self.lines[rowIndex]

  def getCol(self, colIndex):
    colList = []
    for row in self.lines:
      colList.append(row[colIndex])
    return colList

  def getQuadrant(self, quadIndex):
    quadList = []

    startRow = (quadIndex // 3) * 3
    startCol = (quadIndex % 3) * 3

    for i in range(3):
      for j in range(3):
        quadList.append(self.lines[startRow + i][startCol + j])

    return quadList

def containsAllNumbers(line):
    return list(set(['1','2','3','4','5','6','7','8','9']) - set(line)) == []

lines = []
for i in range(9):
    lines.append(input().split())

sudoku = Sudoku()
sudoku.assign(lines)

valid = True
for i in range(9):
    valid = valid and containsAllNumbers(sudoku.getRow(i))
    valid = valid and containsAllNumbers(sudoku.getCol(i))
    valid = valid and containsAllNumbers(sudoku.getQuadrant(i))

if valid:
    print("true")
else:
    print("false")
