'''
Given binary array find max consequtive 1's we get atmost one swap
A = [1,1,0,1,1,1,0,1]
by swaping 0 at 2nd index with 1 in last index we get answer as 6

check notebook for further example
'''

def max_consequtive_ones(arr):
	N = len(arr)

	count_one,count_zero,ans = 0,0,0

	for i in arr:
		if i == 1:
			count_one += 1
		if i == 0:
			count_zero += 1
	if count_one == N:
		return N  
	if count_zero == N:
		return 0

	
	for i in range(N):
		if arr[i] == 0:
			l,r,k = 0,0,0
			j = i-1

			while (j>=0):
				if arr[j] == 1:
					l += 1
				else:
					break
				j = j - 1 

			for j in range(i+1,N):
				if arr[j] == 1:
					r += 1
				else:
					break
			k = l + r

			if (k<count_one): ## checking if any extra ones are there in array to swap
				k = k + 1
				

			if ans < k:
				ans = k 
	return ans
A = [1,1,0,1,1,1,0,1]
print(max_consequtive_ones(A))