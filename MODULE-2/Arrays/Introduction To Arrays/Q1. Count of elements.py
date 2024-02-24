'''
Given an array A of N integers. 
Count the number of elements that have at least 1
elements greater than itself.
Input : A = [3, 1, 2]
Ouput : 2

The elements that have at least 1 element greater than itself are 1 and 2

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
    	count = 0
    	max_element = max(A)

    	for i in range(len(A)):
    		if A[i] < max_element:
    			count += 1
    	return count
