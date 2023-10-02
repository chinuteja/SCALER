'''
Given an array of positive integers A and an integer B, 
find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single integer "-1".
First sub-array means the sub-array for which starting index in minimum.
A = [1, 2, 3, 4, 5]
B = 5
[2, 3]
[2, 3] sums up to 5.

'''
class Solution:
	'''
	Time complexity is O(N**2)
	'''
	def solve(self,A,B):
		output = []
		for i in range(len(A)-1):
			sum_ = 0
			for j in range(i+1,len(A)):
				sum_ += A[i] + A[j]
				if sum_ == B:
					return (A[i:j+1])
		return [-1]

	'''
	time complexity O(N)
	space complexity O(N)
	check notebook for explanation

	'''
	def optimized_solve(self,A,B):
		hm = {}
		hm[0] = -1
		start_index,end_index = -1,-1
		sum_ = 0

		for i in range(len(A)):
			sum_ += A[i]
			if (sum_ - B) in hm:
				start_index = hm[sum_-B] + 1 
				end_index = i
				break
			else:
				hm[sum_] = i

		output = A[start_index:end_index+1]
		if len(output) == 0:
			return [-1]
		return output

sol = Solution()
A = [1, 2, 3, 4, 5]
B = 105

# print(sol.solve(A,B))
print(sol.optimized_solve(A,B))