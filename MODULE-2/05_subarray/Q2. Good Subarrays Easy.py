'''
Given an array of integers A, a subarray of an array is said to be 
good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all 
the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all 
	the elements of the subarray must be greater than B.
RETURN
Your task is to find the count of good subarrays in A.
A = [1, 2, 3, 4, 5]
B = 4
Output : 6
Even length good subarrays = {1, 2}
Odd length good subarrays = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5}

'''
def solve(A,B):

	count = 0
	N = len(A)
	for s in range(N):
		sum_ = 0
		for e in range(s,N):
			sum_ += A[e]
			if ((e-s+1)%2 == 0) and (sum_ < B):
				count += 1
			if ((e-s+1)%2 != 0) and (sum_ > B):
				count += 1
	return count

A = [1, 2, 3, 4, 5]
B = 4
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(solve(A,B))