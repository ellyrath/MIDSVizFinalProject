import csv, json
import sys
from geojson import Feature, FeatureCollection, Point
from operator import itemgetter
from collections import OrderedDict

features = []
topPlaces = {}
yearlist = {}
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rownum = 0
    for line_ in reader: 
        if rownum == 0:
            rownum = 1
            continue
        latitude =  line_[4]
        longitude =  line_[5]
        numkilled = line_[11]
        incidentDate = line_[0]
        temperature_ = line_[29]
        prec_ = line_[30]
        street = line_[7]
        xstreet = line_[8]
        year = incidentDate.split("/")
        year_ = year[2]
        yearlist[year_] = 1
        key_ = longitude + "," + latitude + "," + year_ + "," + street + "," + xstreet + "," + incidentDate 
        if not key_ in topPlaces:
            topPlaces[key_] = 0
        topPlaces[key_] += int(numkilled)
            
print "Dictionary completed"
sortedtopPlaces = OrderedDict(sorted(topPlaces.items(),key=itemgetter(1),reverse=True))

for eachyear in yearlist:
    print eachyear
    itemcount = 0
    for latlong in sortedtopPlaces:
        if not eachyear in latlong:
            continue
        if itemcount == int(sys.argv[3]):
            print itemcount
            break
        print itemcount
        itemcount += 1
        values_ = latlong.split(",")
        eachlatitude = values_[1]
        eachlongitude = values_[0]
        year_ = values_[2]
        street = values_[3]
        xstreet = values_[4]
        peopleKilled = sortedtopPlaces[latlong]
        idate = values_[5]
        latitude, longitude = map(float, (float(eachlatitude), float(eachlongitude)))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'numkilled': peopleKilled,
                    'year': year_, 
                    'street': street,
                    'xstreet': xstreet,
                    'idate': idate,
                    'temp': temperature_,
                    'prec': prec_
                }
            )
        )

print len(features)
collection = FeatureCollection(features)
with open(sys.argv[2],"w") as f:
    f.write('var topaccidents_json = ')
    f.write('%s' % collection)
    f.close()
