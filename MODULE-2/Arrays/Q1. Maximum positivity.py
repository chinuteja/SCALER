'''
Given an array of integers A, of size N.

Return the maximum size subarray of A having only non-negative elements. 
If there are more than one such subarray, return the one having the 
smallest starting index in A.

 A = [5, 6, -1, 7, 8]
O/p :  [5, 6]


'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A):

    	N = len(A)
    	count = 0
    	for i in A:
    		if i> 0:
    			count += 1
    	if count == N :
    		return A

    	start_index,end_index = 0,0

    	i,j = 0,0
    	while((i<N) and (j<N)):
    		if A[j] > 0:
    			j += 1
    			# print(j)
    		else:
    			if (j-i > end_index - start_index +1):
    				start_index = i
    				end_index = j-1
	    		i = i + 1
	    		j = j + 1
    	print(start_index,end_index)
    	return A[start_index:end_index+1]

sol = Solution()
A = [5,6,-1,7,8]

print(sol.solve(A))