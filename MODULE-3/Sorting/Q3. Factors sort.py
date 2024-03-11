'''
You are given an array A of N elements. 
Sort the given array in increasing order of number of distinct factors of 
each element, i.e., 
element having the least number of factors should be the first to be 
displayed and the number having highest number of factors should be the last one.
If 2 elements have same number of factors, then number with less value 
should come first.

A = [6, 8, 9]
Output [9, 6, 8]

A = [2, 4, 7]

Output = [2, 7, 4]
The number 2 has 2 factors, 7 has 2 factors and 4 has 3 factors.

'''
import math
class Solution:

    def count_factors(self,number):

        count = 0
        for i in range(1,int(math.sqrt(number))+1):

            if (number%i) == 0:
                if i == (number//i):
                    count += 1
                else:
                    count += 2
        return count
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        temp = [(a, self.count_factors(a)) for a in A]
        print(temp)
        temp.sort(key=lambda x: (x[1], x[0]))

        for i in range(len(A)):
            A[i] = temp[i][0]
        return A

sol = Solution()
A = [6, 8, 9]
A = [2, 4, 7]
print(sol.solve(A))
