# A = [1,2,3,4,8,10]

# for i in range(0,len(A)):

# 	left_sum,right_sum = 0,0  

# 	for j in range(i):
# 		left_sum += A[j]

# 	for j in range(i+1,len(A)):
# 		right_sum += A[j]

# 	if left_sum == right_sum:
# 		print(True)

# #time complexity O(N**2)

# ## using prefix sum array

# prefix_array = []
# cum_sum = 0
# for i in range(len(A)):
# 	cum_sum += A[i]
# 	prefix_array.append(cum_sum)

# for i in range(len(prefix_array)):
# 	if i == 0:
# 		left_sum = 0
# 	else:
# 		left_sum = prefix_array[i-1]
# 	if i == len(prefix_array):
# 		right_sum = 0
# 	else:
# 		right_sum = prefix_array[len(prefix_array)-1] - prefix_array[i]

# 	if left_sum == right_sum:
# 		print(True) 
# #time complexity O(N)
# ## space comlexity O(N)


output = []
A = [1, 2, 3, 4, 5]
B = [   [0, 2], 
        [2, 4],
        [1, 4]   ]
for inner_list in B:
    start_index = inner_list[0]
    end_index = inner_list[1]
    count  = 0
    while start_index <= end_index:
        if A[start_index]%2 == 0:
            count += 1
        start_index = start_index + 1
    output.append(count)
        
print(output)