import csv, json
import sys
from geojson import Feature, FeatureCollection, Point
from operator import itemgetter
import datetime


accidentsperDay = {}
fatalperday = {}
injuryperday =  {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rownum = 0
    for line_ in reader: 
        if rownum == 0:
            rownum = 1
            continue
        incidentDate = line_[0]
        incidentDate = datetime.datetime.strptime(incidentDate, '%m/%d/%Y').strftime('%Y%m%d') 
        if not incidentDate in accidentsperDay: 
           accidentsperDay[incidentDate] = 0
        accidentsperDay[incidentDate]+= 1

        if not incidentDate in fatalperday: 
           fatalperday[incidentDate] = 0
        if int(line_[10]) <> 0:
           accidentsperDay[incidentDate]+= 1

        if not incidentDate in injuryperday: 
           injuryperday[incidentDate] = 0
        if int(line_[10]) <> 0:
           injuryperday[incidentDate]+= 1


with open(sys.argv[2],"w") as f:
    f.write("Date,Total,Fatal,Injury\n")
    for eachdate in sorted(accidentsperDay):
       outline = eachdate + "," + str(accidentsperDay[eachdate]) + "," + str(fatalperday[eachdate]) + "," + str(injuryperday[eachdate]) + "\n" 
       f.write(outline)
    f.close()

