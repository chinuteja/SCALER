'''
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

The equilibrium index of an array is an index such that the sum of elements at
 lower indexes is equal to the sum of elements at higher indexes.

If there are no elements that are at lower indexes or at higher indexes, 
then the corresponding sum of elements is considered as 0.

A = [-7, 1, 5, 2, -4, 3, 0]

A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

So output is 3
'''
class Solution:
	'''
	Time complexity O(N)
	Space : O(N)
	'''

	def solve(self,A):

		prefix_sum = []
		prefix_sum.append(A[0])

		N = len(A)

		for i in range(1,len(A)):
			prefix_sum.append(prefix_sum[i-1]+A[i])

		for i in range(0,N):
			if i == 0:
				left_sum = 0
			else:
				left_sum = prefix_sum[i-1]
			if i == N-1:
				right_sum = 0
			else:
				right_sum = prefix_sum[N-1] - prefix_sum[i]

			if left_sum == right_sum :
				return i  
		return -1

class Solution:
	# Time : O(N)
	# Space : O(1)

	def solve(self,A):

		total_sum = sum(A)
		left_sum = 0
		right_sum = total_sum

		for i in range(len(A)):

			right_sum = right_sum-A[i]

			if (left_sum == right_sum):
				return i 
			left_sum += A[i]
		return -1