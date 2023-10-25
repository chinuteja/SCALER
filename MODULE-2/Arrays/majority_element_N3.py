'''
You're given a read-only array of N integers. 
Find out if any integer occurs more than N/3 times in the array in 
linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified
 in the process of solving the problem
 INPUT
[1 2 3 1 1]

oUTPUT 1

'''

class Solution:


	def repeatedNumber(self, A):

		if len(A) == 1:
			return A[0]
		first = A[0]
		second = A[1]
		count_1,count_2 = 0,0

		for i in range(2,len(A)):
			if (A[i] == first):
				count_1 += 1
			elif (A[i] == second):
				count_2 += 1

			elif(count_1 == 0):
				first = A[i]
				count_1 = 1
			elif (count_2 == 0):
				second = A[i]
				count_2 = 1
			else:
				count_1 = count_1 - 1
				count_2 = count_2 - 1

		count_1,count_2 = 0,0
		for i in A:
			if i == first:
				count_1 += 1
			if i == second:
				count_2 += 1
		if count_1 > len(A)//3:
			return first
		elif count_2 > len(A)//3:
			return second
		return -1

sol = Solution()
A = [1,2,3,1,1]
print(sol.repeatedNumber(A))

