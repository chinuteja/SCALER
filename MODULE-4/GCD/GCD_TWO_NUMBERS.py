'''
Given 2 non-negative integers A and B, find gcd(A, B)

GCD of 2 integers A and B is defined as the greatest integer 'g' 
such that 'g' is a divisor of both A and B. Both A and B fit in a 32
 bit signed integer.

Note: DO NOT USE LIBRARY FUNCTIONS.

'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
    	'''
    	Time complexity O(log2(max(A,B)))
    	'''

    	if A == 0:
    		return B 
    	if B == 0:
    		return A 

    	return self.gcd(B,A%B)

sol = Solution()
print(sol.gcd(4,6))