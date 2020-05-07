import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

opponent_count = int(input())  # Opponent count

mStartPoint = 0
mRound = 0
lx = 0
ly = 0
def s(x,y):
    global lx
    global ly
    lx=x
    ly=y
# game loop
while True:
    game_round = int(input())
    # x: Your x position
    # y: Your y position
    # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in input().split()]
    for i in range(opponent_count):
        # opponent_x: X position of the opponent
        # opponent_y: Y position of the opponent
        # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in input().split()]
    for i in range(20):
        line = input()  # One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # action: "x y" to move or "BACK rounds" to go back in time
    
    # Vorgehensweise:
    # Moeglichst Viele Zellen in Ecke 
    
    
    p=""
    
    # Go to start point
    if mStartPoint!=1:
        if x!=0:p="0 "+str(y)
        if y!=0:p=str(x)+" 0"
        if x==0 and y==0:mStartPoint=1;s(x,y)
    if mStartPoint==1:
        if lx==0 and ly==0:p="34 0"
        if x==34 and y==0:s(x,y)
        
        if lx==34 and ly==0:p="34 10"
        if x==34 and y==10:s(x,y)
        
        if lx==34 and ly==10:p="0 10"
        if x==0 and y==10:s(x,y)
        
        if lx==0 and ly==10:p="0 19"
        if x==0 and y==19:s(x,y)
        
        if lx==0 and ly==19:p="34 19"
        if x==34 and y==19:s(x,y);mStartPoint=2
    if mStartPoint==2:
        if lx==34 and ly==19:p="34 9"
        if x==34 and y==9:s(x,y)
        
        if lx==34 and ly==9:p="29 9"
        if x==29 and y==9:s(x,y)
        
        if lx==29 and ly==9:p="29 1"
        if x==29 and y==1:s(x,y)
        
        if lx==29 and ly==1:p="24 1"
        if x==24 and y==1:s(x,y)
        
        if lx==24 and ly==1:p="24 18"
        if x==24 and y==18:s(x,y)
        
        if lx==24 and ly==18:p="19 18"
        if x==19 and y==18:s(x,y)
        
        if lx==19 and ly==18:p="19 1"
        if x==19 and y==1:s(x,y)
        
        if lx==19 and ly==1:p="14 1"
        if x==14 and y==1:s(x,y)
        
        if lx==14 and ly==1:p="14 18"
        if x==14 and y==18:s(x,y)
        
        if lx==14 and ly==18:p="9 18"
        if x==9 and y==18:s(x,y)
        
        if lx==9 and ly==18:p="9 1"
        if x==9 and y==1:s(x,y)
        
        if lx==9 and ly==1:p="4 1"
        if x==4 and y==1:s(x,y)
        
        if lx==4 and ly==1:p="4 18"
        if x==4 and y==18:s(x,y)
        
        if lx==4 and ly==18:p="0 18"
        if x==0 and y==18:s(x,y)
        
        if lx==0 and ly==18:p="0 0"
        if x==0 and y==0:s(x,y)
    print(p)
    #Gegner analysieren
    # Naechster Gegner
    
    #print "17 10"
