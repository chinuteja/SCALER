'''

print all the diagonal elements left to right

5   7   3    2   6
11  9   20   21  13
14  -2  3    11  17
27  37  47   50  60



Ouptut 
5
11  7
14  9  3
27 -2 20  2
37  3 21  6
47 11 13
50 17
60 
'''
def printAllDiagonal(A,N,M):

	## print all the elements starting from 0th row

	for j in range(N):
		row = j
		col = 0

		while((row>=0) and (col<N)):
			print(A[row][col],end=" ")
			row -= 1
			col  += 1
		print()

		

	## print elements starting from last col

	for i in range(1,M):
		col = i
		row = N-1

		while((row >= 0) and (col <M)):
			print(A[row][col],end=" ")
			row -= 1
			col += 1
		print()
A = [[5,7,3,2,6],[11,9,20,21,13],[14,-2,3,11,17],[27,37,47,50,60]]
N = 4
M = 5
printAllDiagonal(A,N,M)