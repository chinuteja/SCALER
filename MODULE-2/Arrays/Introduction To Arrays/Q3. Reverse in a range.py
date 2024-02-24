'''
Given an array A of N integers and also given two integers B and C. 
Reverse the elements of the array A within the given inclusive range [B, C].
A = [1, 2, 3, 4]
B = 2
C = 3

Output : [1, 2, 4, 3]

We reverse the subarray [3, 4].

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

    	output = []
    	output = A[B:C+1]
    	return A[:B]+output[::-1]+A[C+1:]

A = [88,17,36,79,60,11,69,49,93,63,86,59,15,92,66,9,70,72,92,83,45,5,21,66,66,68,9,74,16,89,30,54,68,49,57,99,68,39,67,69,31,88,46,64,100,83,93,99,69,45,36,42,46,39,24,17,91,9,29,47,35,94,32,37,57,18,45,19,59,45,70,44,81,27,42,60,56]
print(len(A))
B = 45
C = 73
sol = Solution()
print(sol.solve(A,B,C))