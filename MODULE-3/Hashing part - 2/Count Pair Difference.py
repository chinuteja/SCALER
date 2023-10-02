'''
You are given an array A of N integers and an integer B.
Count the number of pairs (i,j) such that A[i] - A[j] = B and i ≠ j.

Since the answer can be very large, return the remainder after dividing the count 
with 109+7.

A = [1, 2, 1, 2]
B = 1
output 4
The pair which gives difference as 3 are (2, 1), (4, 1), (2, 3) and (4, 3). 
'''
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

    	count = 0
    	hm = {}
    	
    	for i in A:
    		if i not in hm:
    			hm[i] = 1
    		else:
    			hm[i] += 1

    	for i in range(len(A)):
    		if A[i] - B in hm:
    			count += hm[A[i]-B]
    	return count%(10**9+7)

A = [1, 2, 1, 2]
B = 1

sol = Solution()
print(sol.solve(A,B))