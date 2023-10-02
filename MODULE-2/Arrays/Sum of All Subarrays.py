A = [1,2,3]
answer = 0
def findSum(array,start_index,end_index):
    sum_ = 0
    for i in range(start_index,end_index+1):
        sum_ += array[i]
    return sum_


for s in range(len(A)):
    for j in range(s,len(A)):
        answer += findSum(A,s,j)
        # print(A[s:j+1],answer)
print(answer)

print("using contribution technique")

answer = 0
for i in range(len(A)):
    answer += (i+1)*(len(A)-i)*A[i]
print(answer)