'''
Given an array of integers A of size N where N is even.
Divide the array into two subsets such that

1.Length of both subset is equal.
2.Each element of A occurs in exactly one of these subset.

Magic number = sum of absolute difference of corresponding elements of subset.


For Ex:- 
subset 1 = {1, 5, 1}, 
subset 2 = {1, 7, 11}
Magic number = abs(1 - 1) + abs(5 - 7) + abs(1 - 11) = 12

Return an array B of size 2, where B[0] = maximum possible value of 
Magic number modulo 109 + 7, B[1] = minimum possible value of a Magic
number modulo 109 + 7.


Input  A = [3, 11, -1, 5]
 All possible magical numbers:-
 sub1 = {3, 11}, sub2 = {-1, 5}, Magic Number = abs(3 - -1) + abs(11 - 5) = 10
 sub1 = {3, -1}, sub2 = {11, 5}, Magic Number = abs(3 - 11) + abs(-1 - 5) = 14 
 sub1 = {3, 5}, sub2 = {11, -1}, Magic Number = abs(3 - 11) + abs(5 - -1) = 14
 sub1 = {11, -1}, sub2 = {3, 5}, Magic Number = abs(11 - 3) + abs(-1 - 5) = 14
 sub1 = {11, 5}, sub2 = {3, -1}, Magic Number = abs(11 - 3) + abs(5 - -1) = 14
 sub1 = {-1, 5}, sub2 = {3, 11}, Magic Number = abs(-1 - 3) + abs(5 - 11) = 10 
 maximum of all magic number = 14 % 10^9 + 7 = 14
 minimum of all magic number = 10 % 10^9 + 7 = 10

Output  [14, 10]

'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

    	A.sort()
    	min_magic,max_magic = 0,0

    	n = len(A)
    	p1 = 0
    	p2 = len(A)//2
    	mod = 10**9+7

    	while(p2<=len(A)-1):

    		max_magic = ((max_magic%mod) + (abs(A[p2]-A[p1])%mod))%mod
    		p1 += 1
    		p2 += 1
    	for i in range(1,n,2):
    		min_magic += abs(A[i] - A[i-1])

    	# for i in range(n//2):
    	# 	max_magic += abs(A[n//2+i] - A[i])

    	return [max_magic,min_magic]

sol = Solution()
A = [3, 11, -1, 5]
print(sol.solve(A))

