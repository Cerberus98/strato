import json
import random
import sys

points = sys.argv[1]
output = []

for i in xrange(int(points)):
    lat = random.randint(0, 180) - 90
    lon = random.randint(0, 360) - 180
    magnitude = random.random() * 0.2

    output.append(lat)
    output.append(lon)
    output.append(magnitude)

f = open("derp.json", 'w')
f.write(json.dumps([["points", output]]))
f.close()
