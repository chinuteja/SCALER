'''
Given a matrix of integers A of size N x M and an integer B. 
Write an efficient algorithm that searches for integer B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of
the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right

A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3
Output 
    1

 3 is present in the matrix at A[0][1] position so return 1.

'''

class Solution:

    def search(self,A,n,k):

        l = 0
        h = n - 1

        while (l <= h):
            mid = (l + h)//2

            if (A[mid] == k):
                return True
            if (A[mid] <= k):
                l = mid + 1 ## got right
            else:
                h = mid - 1 ## go left
        return False

    def searchMatrix(self, A, B):

        N = len(A[0])

        for inner_list in A:
            if self.search(inner_list,len(inner_list),B):
                return 1
        return 0

A = [ 
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  
    ]
B = 3

A = [   
      [5, 17, 100, 111],
      [119, 120, 127, 131],    
    ]
B = 3

sol = Solution()
print(sol.searchMatrix(A,B))