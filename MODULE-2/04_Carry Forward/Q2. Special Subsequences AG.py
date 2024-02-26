'''
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

Input :
 A = "ABCGAG"
Outpu : 3
 Subsequence "AG" is 3 times in given string 
i.e 0to3,0to5,4to5
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

    	answer,count_A = 0,0

    	for i in A:
    		if i == "A":
    			count_A += 1
    		elif i =="G":
    			answer += count_A
    	return answer
sol = Solution()
A = "ABCGAG"
A = "ACBAGKAGG"
print(sol.solve(A))