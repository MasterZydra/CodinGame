import sys
import math

def getNextPos(startCoord, endCoord, vectorLen):
    # Prevent "ZeroDivisionError: float division by zero"
    if startCoord == endCoord:
        return endCoord
    # Calculate vector v
    v_x = endCoord[0] - startCoord[0]
    v_y = endCoord[1] - startCoord[1]
    # Get length and find multiplicator to norm vector to vectorLen
    len = math.sqrt(v_x**2 + v_y**2)
    mul = abs(vectorLen) / len
    # Norm vector to vectorLen
    v_x *= mul
    v_y *= mul
    # Do vector shift
    return [startCoord[0] + v_x, startCoord[1] + v_y]

def getDistance(coord1, coord2):
    a = max(coord1[0], coord2[0]) - min(coord1[0], coord2[0])
    b = max(coord1[1], coord2[1]) - min(coord1[1], coord2[1])
    c = math.sqrt(a**2 + b**2)
    return c

# Constants
ZOMBIE_SPEED = 400
ASH_SPEED = 1000
ASH_RANGE = 2000

# Save humans, destroy zombies!
# Write an action using print
# To debug: print("Message", file=sys.stderr)

# game loop
while True:
    # Init Ash
    ash_coord = [int(i) for i in input().split()]
    # Init humans
    human_count = int(input())
    humans = []
    for i in range(human_count):
        humans.append([int(j) for j in input().split()])
    # Init zombies
    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        zombies.append([int(j) for j in input().split()])
        #zombies.append(-1)
 
    # Set dist to max posible - (0|0) to (16000|9000)
    lowestDist = 18358
    nearstZomId = -1
    nearstZomId2 = -1
    
    for j in range(human_count):
        human_coord = [humans[j][1], humans[j][2]]
        for i in range(zombie_count):
            zombie_coord = [zombies[i][3], zombies[i][4]]
            
            # Distance from zombie to human
            distZomHum = getDistance(zombie_coord, human_coord)

            # Get next position for Ash
            ash_next = getNextPos(ash_coord, zombie_coord, ASH_SPEED)
            # Get Distance from zombie to Ash
            distZomAsh = getDistance(zombie_coord, ash_next)
            
            ash_next = getNextPos(ash_coord, human_coord, ASH_SPEED)
            distHumAsh = getDistance(ash_next, human_coord)
            
            # Calculate rounds the zombie needs to reach human
            remainingRounds = int(distZomHum/ZOMBIE_SPEED)
            # Calculate rounds Ash needs to reach zombie
            requiredRounds = int((distZomAsh - 0.5 * ASH_RANGE)/ASH_SPEED)
            
            # Check if zombie can be reached before zombie kills the human
            # Or if the zombie is in kill range
            reachable = remainingRounds >= requiredRounds #or distZomAsh <= ASH_RANGE
            
            print("Zombie " + str(zombie_coord), file=sys.stderr)
            print("Remaining: " + str(remainingRounds) + " Required: " + str(requiredRounds), file=sys.stderr)

            if reachable and distZomHum < lowestDist:
                nearstZomId = i
                lowestDist = distZomHum
                nearstZomId2 = j
                print("-> New aim", file=sys.stderr)

            print("DistZomHum: " + str(distZomHum), file=sys.stderr)
            print("Rechable: " + str(reachable) + " - Lowest: " + str(lowestDist), file=sys.stderr)
            print("---------------------", file=sys.stderr)

    # Your destination coordinates
    print(str(zombies[nearstZomId][3]) + " " + str(zombies[nearstZomId][4]))
