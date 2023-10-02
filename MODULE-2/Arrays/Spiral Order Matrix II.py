


def generateMatrix(A):
	
	matrix = []
	if A == 1:
		return [[1]]
	for i in range(A):
		l = []
		for j in range(A):
			l.append(0)
		matrix.append(l)

	i,j = 0,0
	number = 1
	while (A>0):
		# i,j,number = 0,0,0
		### getting N-1 elements from left to right
		for k in range(1,A):
			matrix[i][j] = number
			j += 1
			number += 1

		### getting elements from top to bottom

		for k in range(1,A):
			matrix[i][j] = number
			i += 1
			number += 1

		### getting elements from right to left
		for k in range(1,A):
			matrix[i][j] = number
			j = j - 1
			number += 1

		## getting elements from bottom to top
		for k in range(1,A):
			matrix[i][j] = number
			i = i - 1
			number += 1
		i += 1
		j += 1
		A = A - 2
	if A%2 != 0:
		matrix[i][j] = number
	return matrix
print(generateMatrix(5))



