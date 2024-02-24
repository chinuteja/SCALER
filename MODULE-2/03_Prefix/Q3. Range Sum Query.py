'''
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, 
where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in
A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] 
for each query.


Input : A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]

Output :
[10, 5]
The sum of all elements of A[0 ... 3] = 1 + 2 + 3 + 4 = 10.
The sum of all elements of A[1 ... 2] = 2 + 3 = 5.
'''
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
     ## Time complexit O(N*Q)
    def rangeSum(self, A, B):

    	ans = []

    	for query in B:
    		start = query[0]
    		end = query[1]
    		sum_ = 0
    		for i in range(start,end+1):
    			sum_ += A[i]
    		ans.append(sum_)

    	return ans


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):

    	answer = []
    	N = len(A)
    	prefix_sum = []
    	prefix_sum.append(A[0])

    	for i in range(1,len(A)):
    		prefix_sum.append(prefix_sum[i-1]+A[i])

    	for query in B:
    		start = query[0]
    		end = query[1]

    		if start == 0:
    			answer.append(prefix_sum[end])
    		else:
    			answer.append(prefix_sum[end]-prefix_sum[start-1])
    	return answer


