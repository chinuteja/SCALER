'''

You are given two lowercase strings A and B each of length N. 
Return 1 if they are anagrams to each other and 0 if not.


Note : Two strings A and B are called anagrams to each other 
if A can be formed after rearranging the letters of B.

A = "secure"
B = "rescue"
 Outuput 1

The words CAN be rearranged to form the same word. So, they are  anagrams.


'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

    	if len(A) != len(B):
    		return 0
    	A = ''.join(sorted(A))
    	B = ''.join(sorted(B))

    	print(A,B)

    	for i in range(len(A)):
    		if (A[i] != B[i]):
    			return 0
    	return 1


sol = Solution()
A = "secure"
B = "rescue"
print(sol.solve(A,B))