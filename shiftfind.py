# Base Station Shift Finder
# usage: python3 shiftfind.py oldbaselat oldbaselon newbaselat newbaselon
from math import radians, cos, sin, asin, sqrt
import sys

class rcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

if len(sys.argv) != 5:
    sys.exit(rcolors.FAIL + "Usage: python3 shiftfind.py oldbaselat oldbaselon newbaselat newbaselon")
for i in sys.argv:
    if i != "shiftfind.py":
        if len(i) < 14:
            sys.exit(rcolors.FAIL + "Not enough accuracy: " + i)
        try: 
            dec = float(i)
        except:
            print(rcolors.FAIL + "NaN: " + i)
            sys.exit(rcolors.FAIL + "Usage: python3 shiftfind.py oldbaselat oldbaselon newbaselat newbaselon")


newLat = float(sys.argv[3]) - float(sys.argv[1]) 
newLon = float(sys.argv[4]) -float(sys.argv[2])


lon1 = radians(float(sys.argv[1]))
lat1 = radians(float(sys.argv[2]))
lat2 = radians(float(sys.argv[3]))
lon2 = radians(float(sys.argv[4]))

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
c = 2 * asin(sqrt(a))
    
# Radius of earth in kilometers.
r = 6371
      
# calculate the result
distkm = c * r

newLat = "{:.16f}".format(newLat)
newLon = "{:.16f}".format(newLon)
distm = "{:.4f}".format(distkm/1000)
print(rcolors.HEADER + "\nShift amount:")
print(rcolors.OKBLUE + str(newLat) + " " + str(newLon))
print(rcolors.OKGREEN + "Base survey shift of: " + str(distm) + "m")