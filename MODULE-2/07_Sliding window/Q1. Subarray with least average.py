'''
Given an array A of size N, 
find the subarray of size B with the least average.

Return the index of the first element of the subarray of size B 
that has least average.

A = [3, 7, 90, 20, 10, 50, 40]
B = 3

Output 3 index (from 3 to 5 has least avg)

Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.

'''

def solve(A,k):

	sum_,avg = 0,0
	for i in range(k):
		sum_ += A[i]
	sum_ = avg/k

	answer = avg 
	
	s = 1
	e = k
	min_index = 0
	while (e < len(A)):
		avg = (avg/k) - (A[s-1]/k) + (A[e]/k)
		
		if answer > avg:
			answer = avg
			min_index = s
		s += 1
		e += 1

	return min_index

A = [3, 7, 90, 20, 10, 50, 40]
B = 3

print(solve(A,B))