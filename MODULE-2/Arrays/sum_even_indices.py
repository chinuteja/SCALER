'''
You are given an array A of length N and Q queries given by the 2D array B of size Q*2. 
Each query consists of two integers B[i][0] and B[i][1].
For every query, the task is to calculate the sum of all even indices in the range A[B[i][0]…B[i][1]].

Note : Use 0-based indexing

A = [1, 2, 3, 4, 5]
B = [   [0,2] 
        [1,4]   ]

[4, 8]
The subarray for the first query is [1, 2, 3] whose sum of even indices is 4.
The subarray for the second query is [2, 3, 4, 5] whose sum of even indices is 8.


'''
def sub_array_sum(A,start_index,end_index):
	sum_even = 0
	for i in range(start_index,end_index+1):
		if i%2 == 0:
			sum_even += A[i]
	return sum_even

def solve(A,B):
	'''
	Time complexity O(N**2)
	'''
	output = []

	for inner_list in B:
		start_index = inner_list[0]
		end_index = inner_list[1]
		output.append(sub_array_sum(A,start_index,end_index))
	return output

def solve_optimized(A,B):

	prefix_even_sum = [0 for i in range(len(A))]
	prefix_even_sum[0] = A[0]
	for i in range(1,len(A)):
		if i%2 == 0:
			prefix_even_sum[i] = prefix_even_sum[i-1] + A[i]
		else:
			prefix_even_sum[i] = prefix_even_sum[i-1]
	output = []
	print("prefix_even_sum ",prefix_even_sum)
	for inner_list in B:
		start_index = inner_list[0]
		end_index = inner_list[1]
		if start_index == 0:
			output.append(prefix_even_sum[end_index])
		else:
			output.append(prefix_even_sum[end_index]-prefix_even_sum[start_index-1])
	return output
def main():
	A = [1, 2, 3, 4, 5]
	B = [[0,2],[1,4]]
	A = [2, 1, 8, 3, 9]
	B = [[0,3],[2,4]]
	print(solve_optimized(A,B))
	print(solve(A,B))
if __name__ == '__main__':
	main()