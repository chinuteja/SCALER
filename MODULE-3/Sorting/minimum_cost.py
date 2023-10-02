
def brute_force(A):
	'''
	Time complexity O(N**2)
	'''
	A.sort(reverse=True)
	ans = 0
	for i in range(len(A)):
		for j in range(i,len(A)):
			ans += A[j]
	print(ans)




def solve(A):
	'''
	sorting O(NlogN) 
	Time complexity O(NlogN)
	'''
	A.sort(reverse=True)
	ans = 0
	for i in range(len(A)):
		ans += A[i]*(i+1)
	return ans



def main():
	A = [2,1,4]
	brute_force(A)
	print(solve(A))

if __name__ == '__main__':
	main()