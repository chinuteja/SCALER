'''
Given a binary array i.e can atmost replace
a single 0 with 1 find the maximum consequtive 1's
we can get

A = [1,1,0,1,1,0,1]
replace 0 which is at 2nd index you will get maximum no of 1's
'''
'''
You can atmost replace 0 with 1 and u need to return maximum no of consequitve 1's

For every 0
	find the consequtive 1's on LHS
	find the consequtive 1's on RHS
	if ans < l+r+1:
		ans = l+r+1

'''

def max_consequtive_ones(arr):

	N = len(arr)

	count_one,count_zero = 0,0
	for i in arr:
		if i == 0:
			count_zero += 1
		if i == 1:
			count_one += 1
	## below two if conditinos are edge cases
	if count_one == N:
		return N 
	if count_zero == N :
		return 0

	ans  = 0 
	for i in range(N):
		if arr[i] == 0:
			l = 0
			r = 0
			## chck no of 1s on LHS
			j = i-1
			while j>=0:
				if arr[j] == 1:
					l += 1
				else:
					break
				j = j - 1
			## chck no of 0's on RHS
			
			for j in range(i+1,N):
				if arr[j] == 2:
					r += 1
				else:
					break
			
			if ans < l+r+1:
				ans = l+r+1
	return ans
A = [1,1,0,1,1,0,1]
print(max_consequtive_ones(A))
'''
TIme complexity is O(n) (because of the break statement)

'''