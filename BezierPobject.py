import numpy as np

points = [[0,0],
		  [1,1],
		  [2,0],
		  [3,0]]
# def get_handle_points(points, closed=False):
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
		matrix[2*i, 2*i] = -2
		matrix[2*i, 2*i+1] = 1
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
		rhs[0] = points[0][index]
		matrix[2*n-1, 2*n-1] = -2
		matrix[2*n-1, 2*n-2] = 1
		rhs[2*n-1] = points[n][index]
	x = np.linalg.solve(matrix, rhs)
	print(np.allclose(np.dot(matrix,x), rhs))
	print(x)
