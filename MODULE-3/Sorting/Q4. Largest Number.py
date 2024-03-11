'''
Given an array A of non-negative integers, 
arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a 
string instead of an integer.


 A = [3, 30, 34, 5, 9]
 "9534330"
Input  A = [2, 3, 9, 0]
"9320"


'''
from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if list(set(A)) == [0]:
            return 0
       
        def comparater(a,b):
            a = str(a)
            b = str(b)
            num1 = int(a+b)
            num2 = int(b+a)
            if num1 > num2:
                return -1
            elif num1 < num2:
                return 0
            else:
                return 1
        A = sorted(A, key=cmp_to_key(comparater))
        A = ''.join([str(i) for i in A])
        return A

A = [3, 30, 34, 5, 9]
sol = Solution()
print(sol.largestNumber(A))