'''
You are given an array A of N integers and an integer B. 
Count the number of pairs (i,j) such that A[i] + A[j] = B and i ≠ j.
Since the answer can be very large, return the remainder after dividing the count 
with 109+7.
Note - The pair (i,j) is same as the pair (j,i) and we need to count it only once.
A = [1, 2, 1, 2]
B = 3

The pair which gives sum as 3 are (1, 2), (1, 4), (2, 3) and (3, 4). 
'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

    	count = 0
    	hm = {}
    	for i in range(len(A)):
    		b = B-A[i]
    		if b in hm:
    			count += hm[b]
    		if A[i] in hm:
    			hm[A[i]] += 1
    		else:
    			hm[A[i]] = 1
    	return count%(10**9+7)
sol = Solution()
A = [1, 2, 1, 2]
B = 3
# A = [3, 5, 1, 2]
# B = 8
# A = [1, 2, 1, 2]
# B = 1
print(sol.solve(A,B))

