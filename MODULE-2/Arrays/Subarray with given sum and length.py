
# def solve(A,B,C):

# 	for i in range(len(A)-B+1):
# 		# print("for i ",i)
# 		sum_ = 0
# 		for j in range(B):
# 			# print(j)
# 			sum_ += A[i+j]
# 		# print("*")
# 		if sum_ == C:
# 			return 1
# 	return 0

### sliding window techinque
def solve(A,B,C):
	sum_ = 0 
	for i in range(B):
		sum_ += A[i]

	s,e = 1,B

	while(e<len(A)):
		sum_ = sum_ - A[s-1] + A[e]
		if sum_ == C:
			return 1
		e += 1
		s += 1
	return 0

def main():

	A = [4, 3, 2, 6, 1]
	B = 3
	C = 11

	# A = [4, 2, 2, 5, 1]
	# B = 4
	# C = 6
	print(solve(A,B,C))
if __name__ == '__main__':
	main()

