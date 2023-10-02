A = [-3,6,2,4,5,2,8,-4,3,1]
## = [-3,6,6,6,6,6,8,8,8,8] ## left max array
left_max_array = [A[0]]*len(A)
for i in range(1,len(A)):
	# print(left_max_array[i])
	left_max_array[i] = max(left_max_array[i-1],A[i])
print(left_max_array)

## right max is [8,8,8,8,8,8,8,3,3,1]

# A = [0, 1, 0, 1]
right_max_array = [A[len(A)-1]]*len(A)

i = len(A)-2
while i>=0:
	right_max_array[i] = max(right_max_array[i+1],A[i])
	i = i - 1
print(right_max_array)