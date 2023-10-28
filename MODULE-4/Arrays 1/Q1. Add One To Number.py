'''
Given a non-negative number represented as an array of digits, 
add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the 
head of the list.

NOTE: Certain things are intentionally left unclear in this question 
which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. 
Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? 
Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has 
zeroes before the most significant digit.

Input : [1, 2, 3]
Output : [1, 2, 4]
Explanation:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.

'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
    	
    	count = 0
        for i in A:
            if i == 0:
                count += 1
        if count == len(A):
            return [1]

    	string = ""
    	for i in A:
    		string += str(i)
    	string = string.lstrip("0")

    	output = []
    	ans = int(string)+1
    	ans = str(ans)
    	for i in ans:
    		output.append(int(i))

    	return output
sol = Solution()
A = [1,2,3]
A = [0,0,9,9,9]
print(sol.plusOne(A))