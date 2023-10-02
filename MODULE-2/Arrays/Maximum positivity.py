'''

Given an array of integers A, of size N.

Return the maximum size subarray of A having only non-negative elements. 
If there are more than one such subarray, return the one having the smallest starting index in A.

'''
def solve(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 1:
            count += 1
    if count == len(A):
        return A
    
    max_len = 0
    min_index = 0
    for i in range(len(A)):
        # print("A[i] ",A[i],i)
        if A[i] > 0:
            length = 0
            for j in range(i,len(A)):
                if A[j] > 0:
                    length += 1 

                if A[j] < 0:
                    length = 0

                    break
                # print(length)
            if max_len < length:
                max_len = length
                min_index = i
                # print("max len min_index",max_len,min_index)
                
    return A[min_index:max_len+i]

# A = [5, 6, -1, 7, 8,9]
# print(solve(A))

