# Calculate the volume and surface area of a sphere
# Volume is V=4/3*pi*radius^3
# Area is 4*pi*radius^2

# Get radius as input and make sure it is correct

radius = float(input('enter a radius: '))

print('radius =',radius)

import math

# Calculate area
area = 4*math.pi*math.pow(radius,2)
print ('area =',area)

volume = 4/3*math.pi*math.pow(radius,3)
print ('volume =', volume)



