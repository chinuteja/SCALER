
# A = [0, 1, 0, 1]
# # A = [1, 1, 1, 1]
# # A = [1,1,0,1,0,0,1]
# count = 0
# for i in range(0,len(A)):
#     if A[i] == 0:
#         A[i] = 1
#         for j in range(i+1,len(A)):
#             if A[j] == 0:
#                 A[j] = 1
#             else:
#                 A[j] = 0
#         count += 1
# print(count)

# ### optimized techinque
# A = [0, 1, 0, 1]
# count = 0
# for i in range(len(A)):
#     state = A[i]
#     if count%2 == 0:
#         state = A[i]
#     else:
#         state = 1-A[i]
#     if state == 0:
#         count += 1
# print(count)

max_sum = C[0]
for i in range(A):
    sum_ = C[i]
    for j in range(i+1,A):
        sum_ += C[j]
        if (max_sum < sum_) and sum_ <= B:
            max_sum = sum_
print(max_sum)