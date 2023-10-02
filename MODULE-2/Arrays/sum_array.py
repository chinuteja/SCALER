output = []
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
for smaller_array in B:
    sum_  = 0
    start_index = smaller_array[0]
    end_index = smaller_array[1]
    output.append(sum(A[start_index:end_index+1]))
    # for index in smaller_array:
        # sum_ = sum_ + A[index]
    # output.append(sum_)
print(output)