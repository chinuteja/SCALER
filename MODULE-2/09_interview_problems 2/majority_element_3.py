'''
You're given a read-only array of N integers. 
Find out if any integer occurs more than N/3 times in the array in 
linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Input [1 2 3 1 1]
Output 1

'''
class Solution:

    def repeatedNumber(self, A):

        if len(A) < 3:
            return -1

        first = A[0]
        second = A[1]
        count_1,count_2 = 0,0
        N = len(A)
        for i in range(2,len(A)):

            if A[i] == first:
                count_1 += 1
            if A[i] == second:
                count_2 += 1
            if count_1 == 0:
                count_1 = 1 
                first = A[i]
            if count_2 == 0:
                count_2 = 1 
                second = A[i]
            else:
                count_1 = count_1 - 1
                count_2 = count_2 - 1

        count_1,count_2 = 0,0
        for i in A:
            if i == first:
                count_1 += 1
            if i == second:
                count_2 += 1
        if count_1 > N//3:
            return first
        if count_2 > N//3:
            return second
        return -1

        # print(first,second)

A = [1,2,3,1,1]
A = [1,2,3]

sol = Solution()
print(sol.repeatedNumber(A))