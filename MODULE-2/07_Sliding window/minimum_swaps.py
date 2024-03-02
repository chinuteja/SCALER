'''

Given an array of integers A and an integer B, 
find and return the minimum number of swaps required to bring all 
the numbers less than or equal to B together.

Input
 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Output
2
 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, 
 	A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
'''
def miniswaps(A,B):

	k = 0 ## no of good elements gives the window size
	for i in A:
		if (i <= B):
			k += 1 

	if (k==0) or (k == 1): ## edge cases
		return 1
	bad_elements = 0
	for i in range(k):
		if A[i] > B:
			bad_elements += 1
	answer = bad_elements

	s = 1
	e = k

	while (e<len(A)):
		if A[s-1] > B:
			bad_elements = bad_elements - 1 ## removing bad elemnts A[s-1]
		if A[e] > B: 
			bad_elements = bad_elements + 1 ## add bad elemnts A[e]
		answer = max(answer,bad_elements)

		s += 1
		e += 1
	return answer

A = [1, 12, 10, 3, 14, 10, 5]
B = 8
print(miniswaps(A,B))