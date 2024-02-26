'''
Given an integer array A containing N distinct integers, 
you have to find all the leaders in array A.
 An element is a leader if it is strictly greater than all the elements to
 its right side.

Input :
 A = [16, 17, 4, 3, 5, 2]
Output :
	[17, 2, 5]
Element 17 is strictly greater than all the elements on the right side to it.
 Element 2 is strictly greater than all the elements on the right side to it.
 Element 5 is strictly greater than all the elements on the right side to it.
 So we will return these three elements i.e [17, 2, 5], 
 we can also return [2, 5, 17] or [5, 2, 17] or any other ordering.
'''
class Solution:

	def solve_brute(self,A):

		output = []
		N = len(A)
		for i in range(N-1):
			intial_leader = A[i]
			for j in range(i+1,N):
				if intial_leader < A[j]:
					intial_leader = A[j]
			output.append(intial_leader)
		output.append(A[N-1])

		return list(set(output))

	def solve(self,A):
		N = len(A)
		RM = [-1 for i in range(N)]

		RM[N-1] = A[N-1]

		for i in range(N-2, -1, -1):
			RM[i] = max(RM[i+1],A[i])
		return list(set(RM))


sol = Solution()
A = [16, 17, 4, 3, 5, 2]
print(sol.solve_brute(A))

print(sol.solve(A))