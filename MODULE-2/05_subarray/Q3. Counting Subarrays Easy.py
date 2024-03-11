'''
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.

A = [2, 5, 6]
 B = 10
4

 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},

'''
def solve(A,B):
	count = 0

	for s in range(len(A)):
		sum_ = 0
		for e in range(s,len(A)):
			sum_ += A[e]
			if sum_ < B:
				count += 1
	return count
A = [2,5,6]
B = 10
print(solve(A,B))
