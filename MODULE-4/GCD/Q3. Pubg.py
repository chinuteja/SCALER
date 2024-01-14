'''
There are N players, each with strength A[i]. 
when player i attack player j, player j strength reduces
 to max(0, A[j]-A[i]). When a player's strength reaches zero, 
 it loses the game, and the game continues in the same manner 
 among other players until only 1 survivor remains.

Can you tell the minimum health last surviving person can have?

 A = [2, 3, 4]
Output 
 1
Given strength array A = [2, 3, 4]
 First player attack third player twice. [2, 3, 0]
 First player attack second player. [2, 1, 0]
 Second player attack first player twice. [0, 1, 0]
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
    	ans = 0

    	for i in A:
    		if ans > i:
    			ans = gcd(ans,i)
    		else:
    			ans = gcd(i,ans)
    	return ans
sol = Solution()
A = [2,3,4]
print(sol.solve(A))