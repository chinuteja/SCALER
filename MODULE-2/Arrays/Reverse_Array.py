# array = [-1,4,7,6,-2,7,8,10]
# array = [-1,6,3,2,8,9,10]
# j = len(array)-1
# for i in range(len(array)//2):
# 	array[i],array[j] = array[j],array[i]
# 	j = j -1
# print(array)
# 	# break

## reverse an array at given index
# array = [-3,4,2,8,7,9,6,2,10]
# s_i = 3
# s_j = 7
# while s_i < s_j:
# 	array[s_i],array[s_j] = array[s_j],array[s_i]
# 	s_i += 1
# 	s_j -= 1
# print(array)

# reverse k positions
array = [-2,3,1,4,6,2,8,7,9,3]
k = 1
def reverse(array,start,end):
	while(start < end):
		array[start],array[end] = array[end],array[start]
		start = start + 1
		end = end - 1
	return array
if k >= len(array):
	k = k%len(array)
output_array = reverse(array,0,len(array)-1)
output_array = reverse(output_array,0,k-1)
output_array = reverse(output_array,k,len(array)-1)
print(output_array)