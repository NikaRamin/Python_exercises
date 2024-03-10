# Write a Python program to calculate the distance 
# between the points (x1, y1) and (x2, y2).

import math
p1 = [9,6]
p2 = [8,0]

distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

print("Distance is:",distance)

