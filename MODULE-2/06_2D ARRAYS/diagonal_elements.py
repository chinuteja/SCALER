'''

print all the diagonal elements

5   7   3    2   6
11  9   20   21  13
14  -2  3    11  17
27  37  47   50  60



Ouptut 
5
7 11
3 9 14
2 20 -2 27
6 21 3  37
13 11 47
17 50
60
'''

def printAllDiagonal(A,N,M):

	## print all the elements starting from 0th row

	for j in range(M):
		row = 0
		col = j

		while((row < N) and (col>=0)):
			print(A[row][col],end=" ")
			row += 1
			col -= 1
		print()

	## print elements starting from last col

	for i in range(1,N):
		row = i
		col = M-1

		while((row < N) and (col >=0)):
			print(A[row][col],end=" ")
			row += 1
			col -= 1
		print()
A = [[5,7,3,2,6],[11,9,20,21,13],[14,-2,3,11,17],[27,37,47,50,60]]
N = 4
M = 5
printAllDiagonal(A,N,M)