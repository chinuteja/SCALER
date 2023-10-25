'''
Given a vector A of non-negative integers representing an 
elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Input : A = [0, 1, 0, 2]
Output 1

1 unit is trapped on top of the 3rd element.

'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
		"""
		Time complexity O(N**2)
		Args:
		    A (TYPE): Array of +ve intigers
		
		Returns:
		    TYPE: integer (water trapped)
		"""
		ans = 0

		N = len(A)

		for i in range(1,N-1):

			left = A[i]

			for j in range(i):
				left = max(left,A[j])
			right = A[i]
			for j in range(i+1,N):
				right = max(right,A[j])

			net_support = min(left,right)
			ans += max(net_support-A[i],0)
		return ans

class Solution:
	## in brute force we are taking max of left and right of ith index so 
	## build left max and right max array
	def trap(self,A):
		"""
		Build left max and right max array 
		time complexity O(N)
		space complexity O(N)
		Args:
		    A (TYPE): Array of +ve intigers
		
		Returns:
		    TYPE: ammount of water trapped int
		"""
		n = len(A)
		ans = 0
		lm,rm = [],[]
		for i in range(n):
			lm.append(A[0])
			rm.append(A[n-1])
		
		for i in range(1,n):
			lm[i] = max(lm[i-1],A[i])
		for i in range(n-2,-1,-1):
			rm[i] = max(rm[i+1],A[i])

		for i in range(1,n-1):
			left_max = lm[i]
			right_max = rm[i]

			net_support = min(left_max,right_max)
			ans += max(net_support-A[i],0)
		return ans
sol = Solution()
A = [0, 1, 0, 2]
# A = [-3,6,2,4,5,5,2,8,-4,3,1]
print(sol.trap(A))