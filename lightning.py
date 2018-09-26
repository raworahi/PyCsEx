# Determine the distance to a lightning strike based on the time
# elapsed between the flash and the sound of thunder.
# speed of sound is ~1100ft/sec 1 mile = 5280

# 1 mile distant is 5280/1100 in seconds

import math

time = int(input('number of seconds: '))
speed = 1100
mile = 5280

distance = time*speed/mile

distance = round(distance,2)

print ('Lightning is', distance, 'miles away')
