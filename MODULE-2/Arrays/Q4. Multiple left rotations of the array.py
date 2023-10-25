'''
Given an array of integers A and multiple values in B, 
which represents the number of times array A needs to be left rotated.

Find the rotated array for each value and return the result in the 
from of a matrix where ith row represents the rotated array for the 
ith value in B.

Input :

    A = [1, 2, 3, 4, 5]
    B = [2, 3]
Output :
        [ [3, 4, 5, 1, 2]
     [4, 5, 1, 2, 3] ]
for input 1 -> B[0] = 2 which requires 2 times left rotations

1: [2, 3, 4, 5, 1]

2: [3, 4, 5, 1, 2]

B[1] = 3 which requires 3 times left rotation

1: [2, 3, 4, 5, 1]

2: [3, 4, 5, 1, 2]

2: [4, 5, 1, 2, 4]


'''
class Solution:


    def rotate_left(self,A,rotation):
        for j in range(rotation):
            k = A[0]
            N = len(A)
            # print(A)
            for i in range(1,N):
                A[i-1] = A[i]
            A[N-1] = k
            # print(A)
        return A
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        
        output = []

        for element in B:
            A_copy = A.copy()
            answer = (self.rotate_left(A_copy,element%len(A_copy)))

            output.append(answer)
            # print("answer and output is ",answer,output)
        return output

class Solution:
    '''
    Using slciing
    '''
    def solve(self, A, B):
        n=len(A)
        m=len(B)
        c=[]
        for i in range(m):
            sub_list=[]
            k=B[i]%n
            sub_list=A[k:n]+A[0:k]
            c.append(sub_list)
        return c


    
A = [1, 2, 3, 4, 5]
B = [2,3]

sol = Solution()
print(sol.solve(A,B))

