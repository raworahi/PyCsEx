# Coffee sells at $10.50 a pound plus cost of shipping
# Shipping is $0.86 per pound + $1.50 per shipment

import math

coffee = int(input('How many pounds of coffee would you like? '))

box = coffee*10.5

ship = coffee*.86

pack = 1.5

total = (box+ship+pack)

print ('The total cost of your order is: ', total, 'dollars')
