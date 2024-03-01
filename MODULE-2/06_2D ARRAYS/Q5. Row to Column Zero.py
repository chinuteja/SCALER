'''
You are given a 2D integer matrix A, 
make all the elements in a row or column zero if the A[i][j] = 0. 
Specifically, make entire ith row and jth column zero.

Input 
[1,2,3,4]
[5,6,7,0]
[9,2,0,4]

Output

[1,2,0,0]
[0,0,0,0]
[0,0,0,0]

A[2][4] = A[3][3] = 0, 
so make 2nd row, 3rd row, 3rd column and 4th column zero.

'''

def solve(A):
	row,col = set(),set()

	N = len(A)
	M = len(A[0])

	for i in range(N):
		for j in range(M):
			if A[i][j] == 0:
				row.add(i)
				col.add(j)

	for i in range(N):
		for j in range(M):
			if i in row or j in col:
				A[i][j] = 0
	return A
A = [[1,2,3,4],
[5,6,7,0],
[9,2,0,4]]
print(solve(A))