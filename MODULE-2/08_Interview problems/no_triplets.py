'''
A = [2,6,9,4,10]
count the no of tirplets such that i<j<k and A[i] < A[j] < A[k]

(0,1,2),(0,3,4),(0,2,4),(0,1,4),(1,2,4) ans = 5

regular idea consider 3 for loops TC O(N**3)

'''
'''
Optimized idea make every element as center count
no of elements < that element on LHS
no of elements > that element on RHS
ans = ans + (l*r) 
'''
def count_triplets(A):
	ans = 0
	N = len(A)
	for i in range(1,N-1):
		## count elements on lhs 
		l = 0
		j = i-1
		while (j>=0):
			if A[i] > A[j]:
				l += 1
			j = j - 1
		## count elements on RHS
		r = 0
		for k in range(i+1,N):
			if A[k] > A[i]:
				r += 1
		ans += (l*r)
	return ans 
A = [2,6,9,4,10]
print(count_triplets(A))