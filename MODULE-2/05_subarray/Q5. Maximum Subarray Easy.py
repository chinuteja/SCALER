'''
You are given an integer array C of size A. 
Now you need to find a subarray (contiguous elements) 
so that the sum of contiguous elements is maximum.
But the sum must not exceed B.

A = 5
B = 12
C = [2, 1, 3, 4, 5]

12
We can select {3,4,5} which sums up to 12 which is the maximum possible sum.
return max_sum but not greater than or equal to12

'''

def solve(A,B,C):

	max_sum = 0
	for i in range(A):
		sum_ = 0
		for j in range(i,A):
			sum_ += C[j]

			if (max_sum < sum_) and (sum_ <= B):
				max_sum = sum_
	return max_sum

A = 5
B = 12
C = [2, 1, 3, 4, 5]
print(solve(A,B,C))