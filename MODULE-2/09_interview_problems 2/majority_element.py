'''

Given an array find the majority element
majority element if freq of element is > N/2
eg = 1 6 1 1 2 1
ans = 1
eg = 1 2 3 4 1
ans = none (no elemnt is > N/2)

'''

def brute_force(A,N):
	'''
	Time compleixty O(N**2)
	'''

	for i in range(N):
		freq = 0
		for j in range(N):
			if (A[i] == A[j]):
				freq += 1
		if freq > N//2:
			return A[i]
	return -1

A = [1,6,1,1,2,1]
print(brute_force(A,len(A)))

def optimized(A,N):
	'''
	Time complexity O(N)
	space compleixty O(N)
	'''

	freq = {}

	for i in A:
		if i not in freq:
			freq[i] = 1
		else:
			freq[i] += 1

	# majority_element = -1

	for key in freq:
		if freq[key] > N//2:
			return key
	return -1
A = [1,6,1,1,2,1]
print(optimized(A,len(A)))


def fully_optimzed(A,N):
	'''
	Moores voting algorithm
	time compleixty O(N)
	space complexity O(1)
	'''

	majority = A[0]
	freq = 1
	## first find the majority element
	for i in range(1,N):
		if A[i] == majority:
			freq += 1
		elif (freq == 0):
			freq = 1
			majority = A[i]
		else:
			freq -= 1
	## check if the count of majoirty element is > N/2
	count = 0
	for i in A:
		if i == majority:
			count += 1
	if count > N//2:
		return majority
	return -1
A = [8,6,8,8,2,8]
print(fully_optimzed(A,len(A)))