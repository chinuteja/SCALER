class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        N = len(A)
        prefix_even_sum,prefix_odd_sum = [0 for i in range(N)],[0 for i in range(N)]

        prefix_even_sum[0] = A[0]
        prefix_odd_sum[0] = 0

        for i in range(1,N):
            if i%2 == 0:
                prefix_even_sum[i] = prefix_even_sum[i-1] + A[i]
            else:
                prefix_even_sum[i] = prefix_even_sum[i-1]
        
        for i in range(1,N):
            if i%2 != 0:
                prefix_odd_sum[i] = prefix_odd_sum[i-1] + A[i]
            else:
                prefix_odd_sum[i] = prefix_odd_sum[i-1]
        
        count = 0

        for i in range(N):
            if (i == 0):
                total_even_sum = prefix_odd_sum[n-1] - prefix_odd_sum[i]
                total_odd_sum = prefix_even_sum[n-1] - prefix_even_sum[i]
            else:
                total_even_sum = prefix_even_sum[i-1] +(prefix_odd_sum[n-1] - prefix_odd_sum[i])
                total_odd_sum = prefix_odd_sum[i-1] +(prefix_even_sum[n-1] - prefix_even_sum[i])
            if total_even_sum == total_odd_sum:
                
                count += 1
        return count
