
def LargestNumber(A):
	temp = []
	for number in A:
		while (number != 0):
			remainder = number%10
			temp.append(remainder)
			number = number//10

	temp.sort(reverse=True)
	print(temp)
	ans = ""
	for i in temp:
		ans += str(i)
	return ans

def main():
	A = [3, 30, 34, 5, 9]
	print(LargestNumber(A))

if __name__ == '__main__':
	main()