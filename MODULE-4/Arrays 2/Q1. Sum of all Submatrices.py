'''
Given a 2D Matrix A of dimensions N*N,
 we need to return the sum of all possible submatrices.

 Input 
 A = [ [1, 2]
      [3, 4] ]
 Output : 16
The submatrices are [1], [2], [3], [4], [1, 2], [3, 4], [1, 3], 
[2, 4] and [[1, 2], [3, 4]].
Total sum = 40

'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        """use contribution technique 
        Time complexity is O(n*m)
        
        Args:
            A (TYPE): Description
        """

        no_rows = len(A)
        no_cols = len(A[0])

        sum_ = 0

        for i in range(no_rows):
            for j in range(no_cols):
                sum_ += A[i][j]*(i+1)*(j+1)*(no_rows-i)*(no_cols-j)
        return sum_

sol = Solution()
A = [ [1, 2],[3, 4] ]
print(sol.solve(A))