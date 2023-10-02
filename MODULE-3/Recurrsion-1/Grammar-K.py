'''
On the first row, we write a 0. Now in every subsequent row, 
we look at the previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10.

Given row number A and index B, return the Bth indexed symbol in row A. 
(The values of B are 0-indexed.).

A = 4
row 1 : 0
row 2 : 01
row 3 : 0110
row 4 : 01101001
B = 4
output 1
'''
class Solution:

	def function(self,A):
		if A == 0:
			return [0]

		A = self.function(A-1)
		current = []
		for i in range(len(A)):
			if A[i] == 0:
				current.append(0)
				current.append(1)
			else:
				current.append(1)
				current.append(0)
		return current

	def main(self,A,B):
		output = self.function(A)
		return output[B]
sol = Solution()
print(sol.main(3,0))