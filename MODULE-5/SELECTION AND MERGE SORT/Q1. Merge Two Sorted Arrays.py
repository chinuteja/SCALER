'''
Given two sorted integer arrays A and B, 
merge B and A as one sorted array and return it as an output.

Note: A linear time complexity is expected and you should 
avoid use of any library function.

Input 
A = [4, 7, 9]
B = [2, 11, 19]

Output:
[2, 4, 7, 9, 11, 19]

'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers

    def merge(self,A,B,n,m):

        p1,p2,p3 = 0,0,0 

        C = [0 for i in range(n+m)]

        while((p1< n) and (p2 < m)):
            # print(" p1 ",p1,p2)
            if (A[p1] <= B[p2]):

                C[p3] = A[p1]
                p1 += 1
                p3 += 1
            else:
                C[p3] = B[p2]
                p2 += 1
                p3 += 1

        ### copying the remaining part

        while(p1 < n):
            C[p3] = A[p1]
            p3 += 1
            p1 += 1

        while(p2 < m):
            C[p3] = B[p2]
            p2 += 1
            p3 += 1
        return C


    def solve(self, A, B):
        '''
        Using two pointers method
        Time complexity (O(N+M))
        '''

        C = self.merge(A,B,len(A),len(B))
        return C
sol = Solution()

A = [4, 7, 9]
B = [2, 11, 19]

print(sol.solve(A,B))

X = [94,87,100,11,23,98,17,35,43,66,34,53,72,80,5,34,64,71,9,16,41,66,96]
print(sorted(X))