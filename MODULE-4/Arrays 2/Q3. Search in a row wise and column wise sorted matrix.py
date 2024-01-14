'''
Given a matrix of integers A of size N x M and an integer B.
In the given matrix every row and column is sorted in non-decreasing order.
Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered 
from left to right.
Note 2: If there are multiple B in A then return the smallest value 
of i*1009 +j such that A[i][j]=B.
Note 3: Expected time complexity is linear
Note 4: Use 1-based indexing

Input :
A = [[1, 2]
     [3, 3]]
B = 3
Output :
	2019

A[2][1] = 3
row*1009 + col
2 * 1009 + 1 = 2019
A[2][2] = 3
row*1009 + col
2 * 1009 + 2 = 2020
The minimum value is 2019

'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

    	n = len(A)
    	m = len(A[0])
    	i = 0
    	j = m - 1

    	answer = []
    	while ((i < n) and (j>=0)):
    		if (A[i][j] == B):
    			## adding +1 as we are following 1 indexing
    			value = ((i + 1)*1009) + (j+1)
    			answer.append(value)

    		if (A[i][j] < B):
    			i = i + 1 ## go down

    		else:
    			j = j - 1 ## go left

    	if len(answer) == 0:
    		return -1
    	return min(answer)

sol = Solution()
A = [[1, 2],
	  [3, 3]]
B = 3

print(sol.solve(A,B))