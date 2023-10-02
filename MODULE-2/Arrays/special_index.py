'''
Given an array, arr[] of size N, the task is to find the count of array indices such that 
removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
A=[2, 1, 6, 4]
Output 1

Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 

A=[1, 1, 1]
Output = 3
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.

'''

def solve(A,n):
	prefix_even = [0 for i in range(n)]
	prefix_odd = [0 for i in range(n)]

	prefix_even[0] = A[0]
	for i in range(1,n):
		if i%2 == 0:
			prefix_even[i] = prefix_even[i-1] + A[i]
		else:
			prefix_even[i] = prefix_even[i-1]

	prefix_odd[0] = 0
	for i in range(1,n):
		if i%2 != 0:
			prefix_odd[i] = prefix_odd[i-1] + A[i]
		else:
			prefix_odd[i] = prefix_odd[i-1]

	print("prefix_even ",prefix_even)
	print("prefix_odd ",prefix_odd)
	count = 0
	for i in range(n):
		if i == 0:
			print("i== 0",i)
			sum_even = prefix_odd[n-1] - prefix_odd[0]
			sum_odd = prefix_even[n-1] - prefix_even[0]
			print("sum_odd ,sum_even ",sum_odd,sum_even)
		elif i == n-1:
			print("i == n-1 ",i)
			sum_even = prefix_even[n-2]
			sum_odd = prefix_odd[n-2]
			print("sum_odd ,sum_even ",sum_odd,sum_even)
		else:
			print("i ",i)
			sum_even = prefix_even[i-1] + (prefix_odd[n-1] - prefix_odd[i])
			sum_odd = prefix_odd[i-1] + (prefix_even[n-1] - prefix_even[i])
			print("sum_odd ,sum_even ",sum_odd,sum_even)
		if sum_odd == sum_even:
			# print(i)
			count += 1

	return count
A=[2, 1, 6, 4]
A= [1,1,1]
n = len(A)
print(solve(A,n))