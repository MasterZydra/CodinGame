import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
defis = []
lon = input()
lat = input()
n = int(input())
for i in range(n):
    defib = input()
    defis.append(defib)

def distance(longitubeB, latitudeB, longitudeA, latitudeA):
    longitubeB = float(str(longitubeB).replace(',','.'))
    latitudeB = float(str(latitudeB).replace(',','.'))
    longitudeA = float(str(longitudeA).replace(',','.'))
    latitudeA = float(str(latitudeA).replace(',','.'))
    x = (longitubeB - longitudeA) * math.cos((latitudeA + latitudeB) / 2)
    y = (latitudeB - latitudeA)
    return math.sqrt(x*x + y*y)*6371
p = ''
sd = -1 # Shortest distance

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
for defi in defis:
    defi = defi.split(';')
    dist = distance(lon, lat, defi[4], defi[5])
    if sd == -1 or sd > dist:
        sd = dist
        p = defi[1]
    #print >> sys.stderr, defi
print(p)