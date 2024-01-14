'''
Given an array of integers A of size N that is a 
permutation of [0, 1, 2, ..., (N-1)].

It is allowed to swap any two elements (not necessarily consecutive).

Find the minimum number of swaps required to sort the array in 
ascending order.

A = [1, 2, 3, 4, 0]
There are many ways, to make the array sorted,
 
One of the sequence of swaps as follow: 
    Initial array   ->   [1, 2, 3, 4, 0]
 swapping (1, 2) becomes [2, 1, 3, 4, 0]
 swapping (2, 3) becomes [3, 1, 2, 4, 0]
 swapping (4, 0) becomes [3, 1, 2, 0, 4]
 swapping (3, 0) becomes [0, 1, 2, 3, 4]. 
Thus the array is sorted in 4 swaps.  It cannot be sorted inlesser than 4 swaps.  


'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        count = 0

        for i in range(n):
            while A[i]!=i:
                temp = A[i]
                A[i] = A[A[i]]
                A[temp] = temp
                # A[i], A[A[i]] = A[A[i]], A[i]
                count += 1

        return count
sol = Solution()
A = [1, 2, 3, 4, 0]

print(sol.solve(A))
