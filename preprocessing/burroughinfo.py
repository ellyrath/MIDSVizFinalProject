import csv, json
import sys
from geojson import Feature, FeatureCollection, Point
from operator import itemgetter
from collections import OrderedDict


outdata = {}
numinjured = 'numinjured'
numkilled = 'numkilled' 
pedinjured = 'pedinjured'
pedkilled = 'pedkilled' 
cyclistinjured = 'cyclistinjured'
cyclistkilled = 'cyclistkilled' 
motoristinjured = 'motoristinjured' 
motoristkilled = 'motoristkilled' 
contributingfactor = 'contributingfactor' 
incidentcount = "incidentcount"
burroughs = "burroughs"

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    linecount = 0
    for line_ in reader:
        if linecount == 0:
           linecount = 1
           continue
        incidentDate = line_[0].split("/")
        burrough = line_[2]
        
        year = incidentDate[2] + "," + burrough
        if not year in outdata:
            outdata[year] = {} 
         
         

        if not incidentcount in outdata[year]:
           outdata[year][incidentcount] = 0
        outdata[year][incidentcount] += 1

        if not numinjured in outdata[year]:
            outdata[year][numinjured] = 0
        outdata[year][numinjured] += int(line_[10])

        if not numkilled in outdata[year]:
            outdata[year][numkilled] = 0
        outdata[year][numkilled] += int(line_[11])

        if not pedinjured in outdata[year]:
            outdata[year][pedinjured] = 0
        outdata[year][pedinjured] += int(line_[12])

        if not pedkilled in outdata[year]:
            outdata[year][pedkilled] = 0
        outdata[year][pedkilled] += int(line_[13])

        if not cyclistinjured in outdata[year]:
            outdata[year][cyclistinjured] = 0
        outdata[year][cyclistinjured] += int(line_[14])

        if not cyclistkilled in outdata[year]:
            outdata[year][cyclistkilled] = 0
        outdata[year][cyclistkilled] += int(line_[15])

        if not motoristinjured in outdata[year]:
            outdata[year][motoristinjured] = 0
        outdata[year][motoristinjured] += int(line_[16])

        if not motoristkilled in outdata[year]:
            outdata[year][motoristkilled] = 0
        outdata[year][motoristkilled] += int(line_[17])

        if not contributingfactor in outdata[year]:
            outdata[year][contributingfactor] = {}
        if not line_[18] in outdata[year][contributingfactor]:
           outdata[year][contributingfactor][line_[18]] = 0 
        outdata[year][contributingfactor][line_[18]] += 1 


with open(sys.argv[2],"w") as f:
    f.write("Year,BOROUGH,PersonsInjured,PersonsKilled,PedistriansInjured,PedistriansKilled,CyclistInjured,CyclistKilled,MotoristInjured,MotoristKilled,TopContributingFactor,TotalAccidents\n")
    for eachyear in outdata:
        tfactcount = []
        contfactor = ""
        factcount = 0
        for fact in outdata[eachyear][contributingfactor]:
            tfactcount.append(outdata[eachyear][contributingfactor][fact])
            if outdata[eachyear][contributingfactor][fact] > factcount and not fact == "Unspecified":
                factcount = outdata[eachyear][contributingfactor][fact]
                contfactor = fact  
        print contfactor, factcount, eachyear, max(tfactcount)
        print outdata[eachyear][contributingfactor][contfactor]
        outline = str(eachyear) + "," + str(outdata[eachyear][numinjured]) + "," + str(outdata[eachyear][numkilled]) + "," + str(outdata[eachyear][pedinjured]) + "," + str(outdata[eachyear][pedkilled]) + "," + str(outdata[eachyear][cyclistinjured]) + "," + str(outdata[eachyear][cyclistkilled]) + "," + str(outdata[eachyear][motoristinjured]) + "," + str(outdata[eachyear][motoristkilled]) + "," + contfactor + "," + str(outdata[eachyear][incidentcount]) + "\n" 
        f.write(outline)
    f.close()
