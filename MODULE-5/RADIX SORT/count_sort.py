'''

Sort the array of digits 0-9 in desc order

9 8 4 4 3 2 1 0

Brute force O(NlogN) inbuilt sort function

'''
'''
Idea Maintain a count array 
'''

A = [9,8,4,4,3,2,1,0]
N = len(A)

count = [0 for i in range(10)] ## take the count array of size maximum element +1
for i in range(N):
	count[A[i]] += 1
print(count)

for i in range(9,-1,-1):
	j = 0
	while(j<count[i]):
		print(i,end=" ")
		j += 1 
'''
space O(1) because we are taking array of size 10 only
Time complexity O(N) its not always O(N)
9 = count_9
8 = count_8

0 = count_0
	(count_9 + count_8 + ...+count_0)
	O(N)
'''
