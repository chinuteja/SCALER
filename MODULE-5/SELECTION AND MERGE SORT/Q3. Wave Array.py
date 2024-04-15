'''
Given an array of integers A, 
sort the array into a wave-like array and return it.

In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5..... 


Input 
	A = [1, 2, 3, 4]
Outptu 

	[2, 1, 4, 3]
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
First answer is lexicographically smallest. So, return [2, 1, 4, 3].

Hint: sort the array and swap the adjacent elements
'''


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):

		A.sort()

		for i in range(0,len(A)-1,2):
			A[i],A[i+1] = A[i+1],A[i]
		return A

sol = Solution()
A = [11,8,7,9,2,10,2]
A = [1, 2, 3, 4]
print(sol.wave(A))