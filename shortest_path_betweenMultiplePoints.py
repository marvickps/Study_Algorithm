from distance_between_twoPoints import distance

list_of_points = [[1,3],[2,3],[9,2],[2,9],[4,4]]


# for i in range(len(list_of_points)):
# 	for j in range(len(list_of_points)):
# 		if list_of_points[i] == list_of_points[j]:
# 			pass
# 		else:
# 			print(f'distance between {list_of_points[i]} and {list_of_points[j]} is {distance(list_of_points[i],list_of_points[j])}')
 
for i in range(len(list_of_points)):
    for j in range(i + 1, len(list_of_points)):
        print(f'distance between {list_of_points[i]} and {list_of_points[j]} is {distance(list_of_points[i], list_of_points[j])}')


 # this the optimal solution i could able to find with the time complexity of 
 # O(n^2) {n is the number of points}