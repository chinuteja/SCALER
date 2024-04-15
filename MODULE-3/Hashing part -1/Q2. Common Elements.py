'''

Given two integer arrays, A and B of size N and M, respectively. 
Your task is to find all the common elements in both the array.
Input
A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]

 Output:
 	 [1, 2, 2]

NOTE:

Each element in the result should appear as many times as it appears in 
both arrays.
The result can be in any order.
'''

def solve(A,B):

	hm_A,hm_B = {},{}

	for i in A:
		if i in hm_A:
			hm_A[i] += 1
		else:
			hm_A[i] = 1

	for i in B:
		if i in hm_B:
			hm_B[i] += 1
		else:
			hm_B[i] = 1

	output = []

	for key in hm_A:
		if hm_B.__contains__(key):
			 min_val = min(hm_A[key],hm_B[key])

			 for i in range(min_val):
			 	output.append(key)
	return output

A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
print(solve(A,B))