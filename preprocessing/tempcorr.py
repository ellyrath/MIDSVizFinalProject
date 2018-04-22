import csv, json
import sys
from geojson import Feature, FeatureCollection, Point
from operator import itemgetter
import datetime

temp = {}

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rownum = 0
    for line_ in reader: 
        if rownum == 0:
            rownum = 1
            continue
        if line_[29] == "5":
           continue
        if line_[29] == "-9999.0":
           continue
        if line_[29] == "-17966.20":
           continue
        ttemp = "{0:.2f}".format(float(line_[29]) * 1.8 + 32)
        if float(ttemp) < 0:
           print ttemp
           continue
        ftemp = str(ttemp)
        print ftemp, line_[29] 
        if not ftemp in temp:
           temp[ftemp] = 0
        temp[ftemp] += 1

with open(sys.argv[2],"w") as f:
    f.write("temp,noOfAccidents\n")
    for eachtemp in sorted(temp):
       outline = str(eachtemp) + "," + str(temp[eachtemp]) + "\n" 
       f.write(outline)
    f.close()

