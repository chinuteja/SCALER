'''
Given an array A of N integers. 
Sort the array in increasing order of the value at the tens 
place digit of every number.

If a number has no tens digit, we can assume value to be 0.
If 2 numbers have same tens digit, in that case number with max value will 
come first
Solution should be based on comparator.

Sorted List: [7, 11, 15, 19]
'''
from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
            
        def comparator(a,b):
            a_1 = (a//10)%10
            b_1 = (b//10)%10
            if a_1 < b_1:
                    return -1
            if a_1 > b_1:
                    return 1
            if a_1 == b_1:
                    return b-a
        A = sorted(A, key = cmp_to_key(comparator))

        return A

# Example usage:
A = [15, 11, 7, 19]

sol = Solution()
result = sol.solve(A)
print("Sorted List:", result)

