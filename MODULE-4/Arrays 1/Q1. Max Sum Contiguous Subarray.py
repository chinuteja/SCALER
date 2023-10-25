'''
Find the maximum sum of contiguous non-empty subarray within an array A 
of length N.

A = [1, 2, 3, 4, -10] 
Output : 10
The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 

Output : 6

 The subarray [4,-1,2,1] has the maximum possible sum of 6. 

'''
## Kandede's algorithm
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sum_ = 0
        ans = -10000000000000
        for i in A:
            sum_ += i
            ans = max(sum_,ans)
            if sum_ < 0:
                sum_ = 0
        return ans
