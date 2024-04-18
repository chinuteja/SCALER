class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mod=1000000007
        N=len(A)
        A.sort()
        ans=0
        mi=0#sum of min.m values
        mx=0#sum of max.m values
        for i in range(N):

            mi+=(A[i]%mod *  2**(N-1-i)%mod)  %mod # for smaller elemnts

            mx+=(A[N-1-i]%mod *  2**(N-1-i)%mod)   %mod # for larger elemnts

        ans=(mx-mi)%mod

        return ans