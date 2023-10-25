'''
Given an array, arr[] of size N, the task is to find the count of array indices such that 
removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
A=[2, 1, 6, 4]
Output 1

Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 

A=[1, 1, 1]
Output = 3
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.

'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

    	N = len(A)
    	prefix_even_sum,prefix_odd_sum = [0 for i in range(N)],[0 for i in range(N)]

    	prefix_even_sum[0] = A[0]
    	prefix_odd_sum[0] = 0

    	

    	for i in range(1,N):
    		if i%2 == 0:
    			prefix_even_sum[i] = prefix_even_sum[i-1] + A[i]
    		else:
    			prefix_even_sum[i] = prefix_even_sum[i-1]
    	# print(prefix_even_sum)
    	for i in range(1,N):
    		if i%2 != 0:
    			prefix_odd_sum[i] = prefix_odd_sum[i-1] + A[i]
    		else:
    			prefix_odd_sum[i] = prefix_odd_sum[i-1]


    	count = 0
    	n = N
    	for i in range(N):
    		if (i == 0):
    			total_even_sum = prefix_odd_sum[n-1] - prefix_odd_sum[i]
    			total_odd_sum = prefix_even_sum[n-1] - prefix_even_sum[i]

    		else:
    			total_even_sum = prefix_even_sum[i-1] +(prefix_odd_sum[n-1] - prefix_odd_sum[i])
    			total_odd_sum = prefix_odd_sum[i-1] +(prefix_even_sum[n-1] - prefix_even_sum[i])
    		
    		if total_odd_sum == total_even_sum:
    			count += 1
    	return count


sol = Solution()
A = [2, 1, 6, 4]
A= [1,1,1]
n = len(A)
print(sol.solve(A))