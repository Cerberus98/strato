import json

import pygeoip

points = {}

max_mag = 0
for ip in addresses:
    geo = pygeoip.GeoIP("GeoLiteCity.dat")
    record = geo.record_by_addr(ip)
    latitude = round(record["latitude"], 2)
    longitude = round(record["longitude"], 2)
    coord = (latitude, longitude)
    point = points.get(coord)
    if not point:
        points[coord] = 0
    points[coord] += 1
    if points[coord] > max_mag:
        max_mag = points[coord]

# normalize
output = []
max_mag = float(max_mag)
for coord, magnitude in points.iteritems():
    normalized = points[coord] / max_mag 
    output.append(coord[0])
    output.append(coord[1])
    output.append(normalized)

f = open("derp.json", 'w')
f.write(json.dumps([["points", output]]))
f.close()
