import csv, json
import sys
from geojson import Feature, FeatureCollection, Point

features = []
with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rownum = 0
    for line_ in reader: 
        if rownum == 0:
            rownum = 1
            continue
        latitude =  line_[4]
        longitude =  line_[5]
        temp = line_[29] 
        prec = line_[30] 
        street = line_[7]
        xstreet = line_[8]
        numinjured = line_[10]
        numkilled = line_[11]
        contributingfactor = line_[18]
        vehicle_type = line_[24]
        incidentDate = line_[0]
        incidentTime = line_[1]
        
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'temp': temp,
                    'prec': prec,
                    'street': street,
                    'xstreet': xstreet,
                    'numinjured': numinjured,
                    'numkilled': numkilled,
                    'contributingfactor': contributingfactor,
                    'vehicletype': vehicle_type,
                    'incidentDate': incidentDate,
                    'incidentTime': incidentTime
                }
            )
        )

collection = FeatureCollection(features)
print type(collection)
with open(sys.argv[2],"w") as f:
    print "over here"
    f.write('%s' % collection)
