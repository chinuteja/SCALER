'''
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array 
which we can obtain by deleting zero or more elements from either end of the 
array.
A subarray sum denotes the sum of all the elements of that subarray.

Note : Be careful of integer overflow issues while calculations. 
Use appropriate datatypes.

Input : A = [1, 2, 3]
Output : 20

The different subarrays for the given array are: 
[1], [2], [3], [1, 2], [2, 3], [1, 2, 3].
Their sums are: 1 + 2 + 3 + 3 + 5 + 6 = 20
'''
class Solution:

	# TC = O(N**2)
	def solve(solve,A):
		
		N = len(A)
		sum_ = 0
		for i in range(N):
			sum_ += A[i]
			for j in range(i,N):
				sum_ += A[j]
		return sum_

	def solve_optimized(self,A):
		## using contribution technique
		answer = 0
		N = len(A)
		for i in range(N):
			answer += (i+1)*(N-i)*A[i]
		return answer

A = [1, 2, 3]
sol = Solution()
print(sol.solve_optimized(A))