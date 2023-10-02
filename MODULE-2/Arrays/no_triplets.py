## No of triplets for a given arr[N] elements calculate no of triplets i,j,k such that
# i < j < k and a[i]<a[j]<a[k]

def get_triplets(arr,N):
	"""
	TIme complexity is O(N**3)
	"""

	count = 0
	for i in range(N):
		for j in range(i+1,N):
			for k in range(j+1,N):
				if ((i<j<k) and (arr[i]<arr[j]<arr[k])):
					# print(i,j,k,"===>",arr[i],arr[j],arr[k])
					count += 1
	return count

def get_triplets_optimized(arr,N):
	'''
	Time complexity == O(N**2)
	contribution technique
	'''
	answer = 0
	for j in range(N-1):
		left_side,right_side = 0,0

		## check for elements less tahn LHS
		i = j - 1
		while i >=0 :
			# print(i,j)
			if arr[i] < arr[j]:
				left_side += 1
			i -= 1


		k = j + 1
		while k<N :
			if arr[k] > arr[j]:
				right_side += 1
			k += 1
		answer += left_side*right_side
	return answer

A = [4,1,2,6,9,7]
print(get_triplets(A,len(A)))
print(get_triplets_optimized(A,len(A)))