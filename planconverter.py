"""
Converts QGIS plans into mission planner waypoint files.

Input is a standard plan

Best to simplify alot as mission planner is slow with many points.


"""


readf = input("Input plan file: ")
with open(readf) as readfc:
    lines = readfc.readlines()
writef = input("Ouput MP file name: ")
with open(writef, "x") as writefc:
    writefc.write("QGC WPL 110\n")
    count = 0
    for line in lines:
        x = line.split("\t")
        if count == 0:
            writefc.write("0" + "\t" + "1" + "\t" + "3" + "\t" + "16" + "\t" + "0" + "\t" + "0" + "\t"+ "0" + "\t"+ "0" + "\t" + x[0] + "\t" + x[1] + "\t" + "50" + "\t" + "1" + "\n")
        else:
            writefc.write(str(count) + "\t" + "0" + "\t" + "3" + "\t" + "16" + "\t" + "0.0" + "\t" + "0.0" + "\t"+ "0.0" + "\t"+ "0.0" + "\t" + x[0] + "\t" + x[1] + "\t" + "100.0" + "\t" + "1" + "\n")
        print(x)
        count += 1










writefc.close()
readfc.close()
