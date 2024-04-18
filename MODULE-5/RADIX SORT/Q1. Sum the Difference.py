'''
Given an integer array, A of size N.
You have to find all possible non-empty subsequences of the array of numbers
 and then,
for each subsequence, find the difference between the 
largest and smallest number in that subsequence.
Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

A = [3, 5, 10]

Output  21

All possible non-empty subsets are:
[3]         largest-smallest = 3 - 3 = 0
[5]         largest-smallest = 5 - 5 = 0
[10]        largest-smallest = 10 - 10 = 0
[3, 5]      largest-smallest = 5 - 3 = 2
[3, 10]     largest-smallest = 10 - 3 = 7
[5, 10]     largest-smallest = 10 - 5 = 5
[3, 5, 10]  largest-smallest = 10 - 3 = 7
Sum of the differences = 0 + 0 + 0 + 2 + 7 + 5 + 7 = 21
So, the resultant number is 21 


'''
import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        m=1000000007
        N=len(A)
        A.sort()
        ans=0
        sum_min=0#sum of min.m values
        sum_max=0#sum of max.m values
        for i in range(N):
            sum_max += ( ( A[i]*math.pow(2,i)) % m ) % m
            sum_min += ( ( A[i]*math.pow(2,N-i-1)) % m ) % m

            

        ans=int(sum_max-sum_min)%m

        return ans
A = [3, 5, 10]

sol = Solution()
print(sol.solve(A))