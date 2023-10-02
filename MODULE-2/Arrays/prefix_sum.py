A = [-3,6,2,4,5,2,8,-9,3,1]
Q = [[1,3],[2,7],[4,8],[0,2]]
### find the sum between the query range
for inner_list in Q:
	sum_ = 0
	start_index = inner_list[0]
	end_index = inner_list[1]
	while (start_index <= end_index):
		sum_ += A[start_index]
		start_index += 1
	
	print("Sum between start_index and end_index is ",inner_list,sum_)
## Time compliexity O(Q*N)

## using prefix sum array
prefix_sum = []
cum_sum = 0
for i in range(len(A)-1):
	cum_sum += A[i]
	prefix_sum.append(cum_sum)
print(prefix_sum)

for inner_list in Q:
	start_index = inner_list[0]
	end_index = inner_list[1]
	if start_index == 0:
		print("Sum between start_index and end_index is ",inner_list,prefix_sum[end_index])
	else:
		print("Sum between start_index and end_index is ",inner_list,prefix_sum[end_index]-prefix_sum[start_index-1])
## TIme complixty is O(N +Q)