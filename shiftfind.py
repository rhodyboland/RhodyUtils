# Base Station Shift Finder
from math import radians, cos, sin, asin, sqrt
import csv, sys, statistics

class rcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# usage: conda run shiftfind.py oldbaselat oldbaselon newbaselat newbaselon

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

newLat = "{:.16f}".format(newLat)
newLon = "{:.16f}".format(newLon)
print(rcolors.HEADER + "\nShift amount:")
print(rcolors.OKBLUE + str(newLat) + " " + str(newLon))