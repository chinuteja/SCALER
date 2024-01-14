'''
Given a row-wise and column-wise sorted matrix A of size N * M.
Return the maximum non-empty submatrix sum of this matrix.

Input
    -5 -4 -3
A = -1  2  3
     2  2  4

Output :
    12
Explanation:
The submatrix with max sum is 
-1 2 3
 2 2 4
 Sum is 12.
'''

class Solution:

    def build_prefix_matrix(self, A,n,m):
        """building the prefix matrix
        Time complexity O(n*m)
        Args:
            A (TYPE): matrix
            n (TYPE): no of rows
            m (TYPE): no of columns
        
        Returns:
            TYPE: returns prefix matrix
        """
        ## building prefix matrix
        pf = []
        for rows in range(n):
            l = []
            for cols in range(m):
                l.append(0)
            pf.append(l)

        ## filling first column
        for i in range(n):
            pf[i][0] = A[i][0]
        

        ## col wise sum 
        for i in range(n):
            for j in range(1,m):
                pf[i][j] = pf[i][j-1] + A[i][j]

        ## row wise sum
        for j in range(m):
            for i in range(1,n):
                pf[i][j] = pf[i-1][j] + pf[i][j]

        return pf

    def sum(self,pf,a1,b1,a2,b2):
        """finding the sum
        TC : O(1)
        Args:
            pf (TYPE): prefix matrix
            a1,b1 (TYPE): top left cordinates
            a2,b2 : bottom right cordinates
        
        Returns:
            TYPE: Description
        """
        sum_ = pf[a2][b2]

        if(b1 - 1) >= 0:
            sum_ -= pf[a2][b1-1]
        if (a1 - 1) >= 0:
            sum_ -= pf[a1-1][b2]
        if ((a1 - 1) >= 0) and ((b1 - 1) >= 0):
            sum_ += pf[a1-1][b1-1]

        return sum_


    def solve(self, A):

        n = len(A)
        m = len(A[0])

        pf = self.build_prefix_matrix(A,n,m)
        
        ans = -10000000000

        for i in range(len(A)):
            for j in range(len(A[0])):
                sum_ = self.sum(pf,i,j,n-1,m-1)
                ans = max(ans,sum_)
        return ans

        
        

A = [[-5,-4,-3],[-1,2,3],[2,2,4]]
A = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.solve(A))
