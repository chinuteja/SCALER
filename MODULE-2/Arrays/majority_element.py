'''
Given an array of size N return element that exits a majorit
i.e element freq > N/2
A = [1,6,1,1,2,1]
outpt is 1 whos feq is > N/2

'''
def bruteforce(A,N):
	'''
	Time complexity is O(N**2)

	'''
	for i in range(N):
		count = 0
		for j in range(i,N):
			if A[i] == A[j]:
				count += 1
		if count > N//2:
			return A[i]
	return -1

def optimized(A,N):
	'''
	Time complexity is O(N)
	'''

	majority = A[0]
	freq = 1
	for i in range(1,N):
		if A[i] == majority:
			freq += 1
		else:
			if freq == 0:
				majority = A[i]
				freq = 1
			else:
				freq = freq -1

	count = 0
	for i in range(N):
		if A[i] == majority:
			count += 1
	if count > N//2:
		return majority
	return -1

def main():
	A = [1,6,1,1,2,1]
	A = [3,3,4,4,3]
	A = [3,4,3,6,1,3,2,5,3,3,3]
	A = [4,6,5,3,4,5,6,4,4,4]
	A = [1,1,1,2,2]
	A = [1,2,3,1,1]

	# print(optimized_new(A,len(A)))
	print(optimized(A,len(A)))
if __name__ == '__main__':
	main()


# A = [2,3,1,-1,0,8,5,4]
# s,e,event = 3,6,"O"
# s,e,event = 1,5,"E"
# sum_odd,sum_even = 0,0
# for i in range(s,e+1):
# 	if event == "O":
# 		if i%2 != 0:
# 			sum_odd += A[i]
# 	elif i%2 == 0:
# 		sum_even += A[i]
# if event == "O":
# 	print(sum_odd)
# else:
# 	print(sum_even)