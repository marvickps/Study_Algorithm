import math

def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

print(distance([3,2],[4,4]))