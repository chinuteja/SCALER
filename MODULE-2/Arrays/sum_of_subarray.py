# ## find sum of all subarrays
# ## brute force
# A = [3,2,-1,4]
# def find_sum_subarray(start_index,end_index,A):
#     sum_ = 0
#     for i in range(start_index,end_index+1):
#         sum_ += A[i]
#     print("sub array is ",A[start_index:end_index+1],"==>",sum_)
#     return sum_
# for s in range(len(A)):
#     for e in range(s,len(A)):
#         # sum_ = 0
#         find_sum_subarray(s,e,A)



# print("** Optimized Code **")
# # A = [3,2,-1,4]
# # for s in range(len(A)):
# #   sum_ = A[s]
# #   print([A[s]],"==>",sum_)
# #   for e in range(s+1,len(A)):
# #       # print(sum_)
# #       sum_ += A[e]
# #       # print(A[e])
# #       print(A[s:e+1],"==>",sum_)
# A = [3,2,-1,4]
# for s in range(len(A)):
#     sum_ = 0
#     for e in range(s,len(A)):
#         sum_ += A[e]
#         print(A[s:e+1],"==>",sum_)
# '''
# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one 
# of the criteria:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must 
# be greater than B.
# Your task is to find the count of good subarrays in A.
# '''
# A = [1, 2, 3, 4, 5]
# B = 4
# A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
# B = 65
# count = 0
# for s in range(len(A)):
#     sum_ = 0
#     for e in range(s,len(A)):
#         sum_ += A[e]

#         if (s-e+1)%2 == 0:
#             if sum_ < B:
#                 count += 1
#         elif sum_ > B:
#             count += 1
# print("good subarray are ",count)

# A = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# print(A)
# for i in range(len(A[0])):
#     for j in range(i+1,len(A)):
#         temp = A[i][j]
#         # temp_2  = A[j][i]
#         # print("A[i][j]",temp,A[j][i])
#         # print("A[j][i] ",A[j][i],temp_1)
        
#         A[i][j] = A[j][i]
#         A[j][i] = temp
#         # print(A)
# print(A)
### 90 degrees rotation
# A =  [
#     [1, 2],
#     [3, 4]
#  ]
# print(A)
# for i in range(len(A)):
#     for j in range(i+1,len(A)):
#         A[i][j],A[j][i] = A[j][i],A[i][j]
# output_matix = []
# # print("hello")
# print(A)
# for row in A:
#     output_matix.append(row[::-1])
# print(output_matix)