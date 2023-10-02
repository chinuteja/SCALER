import math
def function(N):
	for i in range(1,N+1):
		# print(math.sqrt(N))
		if (i*i) == N:
			return True
	return False
print(function(36))