'''
You are given an array A of N elements. 
You have to make all elements unique. 
To do so, in one step you can increase any number by one.

Find the minimum number of steps.

 A = [1, 1, 3]
 We can increase the value of 1st element by 1 in 1 step and 
 will get all unique elements. i.e [2, 1, 3].

'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

    	A.sort()
    	ans = 0
    	for i in range(1,len(A)):

    		if (A[i] <= A[i-1]):
    			ans += A[i-1] - A[i] + 1 ## update no of moves
    			A[i] = A[i-1] + 1 ## update array by 1
    	return ans

sol = Solution()
A = [1, 1, 3]
A = [1,1,1,1]
print(sol.solve(A))