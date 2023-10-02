# Given a binary array we can atmost replace zero with one find the most consequitive ones we get
#eg : [1,1,0,1,1,0,1]
## if we replace 0 with 1 in the 2nd index we get maximum consequtive 1's so answer is 5

def get_consequtive_ones(arr,N):
	'''
	This is brute force method with time complexity O(N)
	'''
	count = 0
	for i in arr:
		if i == 1:
			count += 1
	if count == N:
		return 0
	if count == 0:
		return 1

	answer = 0
	for i in range(N):
		left,right = 0,0
		### find left side consequtive 1's
		if arr[i] == 0:

			j = i - 1
			while(j >= 0):
				if arr[j] == 1:
					left += 1
				else:
					break
				j -= 1
			## find right side consequtive 1's
			k = i + 1
			while (k < N):
				if arr[k] == 1:
					right += 1
				else:
					break
				k += 1
			answer = max(answer,left+right+1)
			# ones = left + right
			# print("ones ",ones)
			# if (ones < count):
			# 	ones += 1
	return answer
A = [1,1,0,1,1,0,1]
print(get_consequtive_ones(A,7))
