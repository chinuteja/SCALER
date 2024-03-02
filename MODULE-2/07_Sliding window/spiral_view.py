# import numpy as np
'''
spiral view

1   2   3  x
4   5   6  y
7   8   9  z
10  11  12 a

spiral view
1 2 3 x y z a 12 10 7 4 5 6 9 8
// printing boundary eleemnts
'''
def solve(A):
	i,j = 0,0
	N = len(A)

	while(N>1): ## loop goes through inner boundaries

		## print elements from left to right
		for k in range(1,N):
			print(A[i][j],end=" ")
			j += 1
		## elements from top to down
		for k in range(1,N):
			
			print(A[i][j],end=" ")
			i += 1
		## elements from right to left
		for k in range(1,N):
			print(A[i][j],end=" ")
			j = j - 1
		## elements from down to top
		for k in range(1,N):
			print(A[i][j],end=" ")
			i = i - 1
		N = N-2
		i += 1
		j += 1
		# print()
		# print("i,j after N",N,i,j)
		if N == 1:
			print(A[i][j]) ## center element
A = []
# Define the dimensions of the matrix
rows, cols = 5, 5

# Initialize a counter
counter = 1

# Generate a square matrix of size 5x4 with numbers from 1 to 20
matrix = [[counter + col + (row * cols) for col in range(cols)] for row in range(rows)]

# Display the generated matrix
for row in matrix:
    print(row)
print("spiral view")
solve(matrix)