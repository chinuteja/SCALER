




def make_zero(A,fixed_row,fixed_column,total_rows,total_columns):
	col_index = 0
	row_index = 0
	while (col_index < total_columns):
		A[fixed_row][col_index] = 0
		col_index += 1
	while (row_index < total_rows):
		A[row_index][fixed_column] = 0
		row_index += 1
# def solve(A):
# 	total_rows = len(A)
# 	total_columns = len(A[0])
# 	for i in range(total_rows):
# 		for j in range(total_columns):
# 			if (A[i][j] == 0):
# 				make_zero(A,i,j,total_rows,total_columns)
# 	return A
def solve(a):
    rows, cols = set(), set()
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                rows.add(i)
                cols.add(j)
    # print("rows and cols ",rows,cols)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i in rows or j in cols:
                a[i][j] = 0

    return a
A = [[1,2,3,4],[5,6,7,0],[9,2,0,4]]
print(solve(A))
##maximum sum of subarray
# A = [-3,4,-2,5,3,-2,8,2,-1,4]
# k = 5
# max_sum = 0
# for i in range(k):
# 	sum_ = 0
# 	for j in range(i,k+i):
# 		sum_ += A[j]
# 	if max_sum < sum_:
# 		max_sum = sum_
# print(max_sum)

