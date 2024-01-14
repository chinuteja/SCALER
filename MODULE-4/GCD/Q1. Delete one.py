'''
Given an integer array A of size N. 
You have to delete one element such that the GCD(Greatest common divisor) 
of the remaining array is maximum.

Find the maximum value of GCD.


Input :
 A = [12, 15, 18]

Output :
	6
If you delete 12, gcd will be 3.
 If you delete 15, gcd will be 6.
 If you delete 18, gcd will 3.
 Maximum value of gcd is 6.
'''
def gcd(A,B):
    if B==0:
        return A
    else:
        return gcd(B, A%B)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

    	N = len(A)
    	prefix_gcd = [0 for i in range(N)]
    	sufix_gcd = [0 for i in range(N)]

    	prefix_gcd[0] = A[0]

    	for i in range(1,N):
    		prefix_gcd[i] = gcd(max(prefix_gcd[i-1],A[i]),min(prefix_gcd[i-1],A[i]))

    	sufix_gcd[N-1]  = A[N-1]
    	for i in range(N-2,-1,-1):
    		sufix_gcd[i] = gcd(max(sufix_gcd[i+1],A[i]),min(sufix_gcd[i+1],A[i]))
    	
    	answer = 0
    	# print(prefix_gcd)
    	# print(sufix_gcd)
    	for i in range(0,N):
    		if i == 0:
    			value = sufix_gcd[i+1]
    		elif i == N-1:
    			value = prefix_gcd[i-1]
    		else:
    			value = gcd(prefix_gcd[i-1],sufix_gcd[i+1])
    		answer = max(answer,value)
    	return answer


sol = Solution()
A = [5, 15, 30]
print(sol.solve(A))