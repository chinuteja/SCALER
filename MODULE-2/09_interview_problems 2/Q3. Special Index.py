'''
Given an array, arr[] of size N, 
the task is to find the count of array indices such that 
removing an element from these indices makes the sum of 
even-indexed and odd-indexed array elements equal.

Input A = [2, 1, 6, 4]

Output 1

Removing arr[1] from the array modifies arr[] to
{ 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 

Therefore, the required output is 1. 

'''

def solve(A):

	N = len(A)
	# build odd,even prefix arrays
	prefix_even,prefix_odd = [],[]

	prefix_even.append(A[0])
	prefix_odd.append(0)

	for i in range(1,N):
		if (i%2 == 0):
			prefix_even.append(prefix_even[i-1]+A[i])
		else:
			prefix_even.append(prefix_even[i-1])

	for i in range(1,N):
		if (i%2 != 0):
			prefix_odd.append(prefix_odd[i-1]+A[i])
		else:
			prefix_odd.append(prefix_odd[i-1])
	sum_even,sum_odd,count = 0,0,0
	for i in range(N):

		if i == 0:
			sum_even = prefix_odd[N-1] - prefix_odd[0]
			sum_odd = prefix_even[N-1] - prefix_even[0]
		elif i == N-1:
			sum_even = prefix_even[N-2]
			sum_odd = prefix_odd[N-2]

		else:
			sum_even = prefix_even[i-1] + (prefix_odd[N-1] - prefix_odd[i])
			sum_odd = prefix_odd[i-1] + (prefix_even[N-1] - prefix_even[i])

		if sum_even == sum_odd:
			count += 1
	return count

A = [2, 1, 6, 4]
A = [1, 1, 1]

print(solve(A))