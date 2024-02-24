import math
def count_factors(N):
	count = 0
	
	if N == 1:
		return 1

	for i in range(1,int(math.sqrt(N))+1):
		if N%i == 0:
			count = count + 2
	return count

def main():
	print("Enter an Integer ")
	N = int(input())
	print("No of factors ",N," has are ",count_factors(N))
if __name__ == '__main__':
	main()