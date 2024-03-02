'''
Given array of N elements find the max sum subarry of lenght k
A = [-3,4,-2,5,3,-2,8,2,-1,4] k = 5

Answer is  16 i.e 
elements between 3rd and 7th index

'''
def solve(A,N,k):
	'''
	Time complexity O(N)
	{fixed length + carry forward == sliding window}

	'''

	sum_ = 0
	for i in range(0,k):
		sum_ += A[i]

	s = 1
	e = k
	ans = sum_
	while (e < N):
		sum_ = sum_ - A[s-1] + A[e]

		ans = max(ans,sum_)

		s += 1
		e += 1
	return ans 

A = [-3,4,-2,5,3,-2,8,2,-1,4] 
k = 5
print(solve(A,len(A),k))