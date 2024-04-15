'''
Given an array of integers A. If i < j and A[i] > A[j], 
then the pair (i, j) is called an inversion of A. 
Find the total number of inversions of A modulo (109 + 7).

A = [3, 4, 1, 2]


Output 4

The pair (0, 2) is an inversion as 0 < 2 and A[0] > A[2]
The pair (0, 3) is an inversion as 0 < 3 and A[0] > A[3]
The pair (1, 2) is an inversion as 1 < 2 and A[1] > A[2]
The pair (1, 3) is an inversion as 1 < 3 and A[1] > A[3]

'''

class Solution:


    def merge(self,A,s,m,e):

        count = 0
        p1 = s 
        p2 = m + 1
        p3 = 0

        temp = [0 for i in range(e-s+1)]

        while(p1<= m and p2<=e):

            if (A[p1] <= A[p2]):

                temp[p3] = A[p1]
                p1 += 1
                p3 += 1
            else:
                count  += m - p1 + 1
                temp[p3] = A[p2]
                p2 += 1
                p3 += 1 

        while (p1<=m):
            temp[p3] = A[p1]
            p1 += 1
            p3 += 1
        while (p2<=e):
            temp[p3] = A[p2]
            p2 += 1
            p3 += 1

        counter = 0
        for i in range(s,e  +1):
            A[i] = temp[counter]
            counter += 1
        return count

    def invcount(self,A,s,e):

        if (s == e):
            return 0
        mid = (s+e)//2

        x = self.invcount(A,s,mid)
        y = self.invcount(A,mid+1,e)
        z = self.merge(A,s,mid,e)

        return x + y + z

    def solve(self, A):

        ans = self.invcount(A,0,len(A)-1)

        return ans

sol = Solution()

A = [3, 4, 1, 2]
print(sol.solve(A))

