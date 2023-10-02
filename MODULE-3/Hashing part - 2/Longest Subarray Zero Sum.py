'''
Given an array A of N integers.
Find the length of the longest subarray in the array which sums to zero.

Input : A = [1, -2, 1, 2]
Output : 3
 [1, -2, 1] is the largest subarray which sums up to 0.


'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        pf = []
        pf.append(A[0])
        for i in range(1, len(A)):
            pf.append(pf[i-1] + A[i])

        hm = {}

        N = len(pf)

        ans = 0
        for i in range(N):
            if pf[i] not in hm:
                hm[pf[i]] = i

            elif pf[i] in hm:
                ans = max(ans,i-hm[pf[i]])
            if pf[i] == 0:
                ans = max(ans,hm[pf[i]]+1)
        return ans


sol = Solution()
A = [1,-1,2,-2,3,-1,4,-3]
# A = [1, -2, 1, 2]

print(sol.solve(A))