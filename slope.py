# Two points on a place are specified
# using coordinates (x1,y1) and (x2,y2)
# calculate the slope of the line through the points

# Slope = rise over run

x1 = int(input('Enter first X coordinate:'))
y1 = int(input('Enter first Y coordinate:'))
x2 = int(input('Enter second X coordinate:'))
y2 = int(input('Enter second Y coordinate:'))

rise = y2 - y1
run = x2 - x1

slope = rise/run

print ('Slope is: ', slope)

     
