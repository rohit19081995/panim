import numpy as np

points = [[1,0],
		[2,1],
		[3,0],
		[4,0],]
# def get_handle_points(points, closed=False):
handle_points = []
closed = False
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
		rhs[0] = points[0][index]
		matrix[2*n-1, 2*n-1] = 4
		matrix[2*n-1, 1] = -2
		matrix[2*n-1, 2*n-2] = 1
		rhs[2*n-1] = -4*points[0][index]

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
