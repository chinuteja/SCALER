'''
Given an array A, find the size of the smallest subarray such that it 
contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

Input A = [1, 3, 2]
Outut 2

 Take the 1st and 2nd elements as they are the minimum and maximum 
 elements respectievly.

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

    	max_val = max(A)
    	min_val = min(A)

    	answer = len(A)
    	N = len(A)
    	if (max_val == min_val):
    		return 1
    	for i in range(N):

    		if (A[i] == max_val):
    			for j in range(i+1,N):
    				if (A[j]==min_val):
    					answer = min(answer,j-i+1)
    					break
    		if (A[i] == min_val):
    			for j in range(i+1,N):
    				if (A[j] == max_val):
    					answer = min(answer,j-i+1)
    					break
    	return answer

A = [1, 3, 2]
A = [2, 6, 1, 6, 9]
A = [4,4,4,4]
sol = Solution()
print(sol.solve(A))