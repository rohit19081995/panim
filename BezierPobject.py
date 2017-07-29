import numpy as np

# points = [[1,0],
# 		[2,0],
# 		[3,0],
# 		[4,0],
# 		[4,1],
# 		[4,2],
# 		[4,3],
# 		[3,3],
# 		[2,3],
# 		[1,3],
# 		[1,2],
# 		[1,1],
# 		[1,1],
# 		[1,0]]
# points = [[1,1], [1,0], [2,0]]
points = []
for i in range(5):
	points.append([np.cos(-i/5*2*np.pi), np.sin(-i/5*2*np.pi)])

points.append(points[0])
print(points[0], points[-1])
# def get_handle_points(points, closed=False):
handle_points = []
closed = True
n = len(points)-1
for index in range(len(points[0])):
	print(index)
	matrix = np.zeros((2*n,2*n))
	rhs = np.zeros(2*n)
	for i in range(1,n):
		matrix[2*i-1,2*i] = 1
		matrix[2*i-1,2*(i-1)+1] = 1
		rhs[2*i-1] = 2*points[i][index]
		matrix[2*i, 2*i] = 2
		matrix[2*i, 2*i+1] = -1
		matrix[2*i, 2*(i-1)] = 1
		matrix[2*i, 2*(i-1)+1] = -2

	if closed:
		matrix[0, 0] = 1
		matrix[0, 2*n-1] = 1
		rhs[0] = 2*points[0][index]
		matrix[2*n-1, 0] = -2
		matrix[2*n-1, 1] = 1
		matrix[2*n-1, 2*n-1] = 2
		matrix[2*n-1, 2*n-2] = -1
		rhs[2*n-1] = 0

	else:
		matrix[0, 0] = -2
		matrix[0, 1] = 1
		rhs[0] = -points[0][index]
		matrix[2*n-1, 2*n-1] = -2
		matrix[2*n-1, 2*n-2] = 1
		rhs[2*n-1] = -points[n][index]
	print(matrix)
	print(rhs)
	handle_points.append(np.linalg.solve(matrix, rhs))

handle_points = np.array(handle_points).swapaxes(0,1)
p1arr = handle_points[::2]
p2arr = handle_points[1::2]
svg_string = 'M %f,%f' % (points[0][0], points[0][1])
for i in range(n):
	svg_string += 'C %f,%f %f,%f %f,%f' % (p1arr[i][0], p1arr[i][1], p2arr[i][0], p2arr[i][1], points[i+1][0], points[i+1][1])

point_string = ''
for point in points:
	point_string += '<circle cx="%f" cy="%f" r="0.003" stroke="black" stroke-width="0.03" fill="red"/>' % (point[0], point[1])