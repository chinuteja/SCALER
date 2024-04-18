'''

Given an array A of non-negative integers of size N. 
Find the minimum sub-array Al, Al+1 ,..., Ar 
such that if we sort(in ascending order) that sub-array, 
then the whole array should get sorted. If A is already sorted, output -1.

A = [1, 3, 2, 4, 5]

[1, 2]

If we sort the sub-array [A1, A2] then the whole array A gets sorted.
'''

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):

		B = sorted(A)
		start,end = -1,-1
		N = len(A)

		for i in range(N):
			if A[i] != B[i]:
				start = i  
				break
		for i in range(N-1,-1,-1):
			if A[i] != B[i]:
				end = i 
				break
		if start == end:
			return [-1]
		return [start,end]


A = [1, 3, 2, 4, 5]
A = [1, 2, 3, 4, 5]

sol = Solution()
print(sol.subUnsort(A))