'''
You are given a large number in the form of a array A of size N 
where each element denotes a digit of the number.

You are also given a number B. You have to find out the value of A % B and
 return it.

A = [1, 4, 3]
B = 2

Output :
1
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        string = ""
        for i in A:
            string += str(i)
        return int(string)%B

sol = Solution()
A = [1, 4, 3]
B = 2

A = [4, 3, 5, 3, 5, 3, 2, 1]

B = 47
print(sol.solve(A,B))