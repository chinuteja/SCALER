'''
Given a number A, check if it is a magic number or not.

A number is said to be a magic number if the sum of its digits is calculated till a 
single digit recursively by adding the sum of the digits after every addition. 
If the single digit comes out to be 1, then the number is a magic number.

Sum of digits of (83557) = 28
 Sum of digits of (28) = 10
 Sum of digits of (10) = 1. 
 Single digit is 1, so it's a magic number. Return 1.


 Sum of digits of (1291) = 13
 Sum of digits of (13) = 4
 Single digit is not 1, so it's not a magic number. Return 0.

'''

class Solution:
    # @param A : integer
    # @return an integer
    def magic(self, A):
    	if A < 10:
    		return A
    	sum_ = 0
    	while (A>0):
    		sum_ += A%10
    		A = A//10

    	return self.magic(sum_)
    
    def solve(self,A):
        output = self.magic(A)
        if output == 1:
            return 1
        return 0
sol = Solution()
print(sol.solve(83557))