# def sum_of_digits(number):
# 	sum_ = 0
# 	while (number != 0):
# 		sum_ += number%10
# 		number = number//10
# 	return sum_
# def sum_of_digits_recursion(number):
# 	if number == 0:
# 		return 0
# 	# sum_ += 
# 	return number%10 + sum_of_digits_recursion(number//10)
# def main():
# 	print(sum_of_digits_recursion(46))
# if __name__ == '__main__':
# 	main()

def reverse(string,index):
	if index == 0:
		return ""

	return string[index-1]+reverse(string,index-1)
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    string = input()
    output = reverse(string,len(string))
    print(output)
    return output 

if __name__ == '__main__':
    main()
#