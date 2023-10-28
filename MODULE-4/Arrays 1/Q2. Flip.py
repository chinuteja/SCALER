'''
Problem Description
You are given a binary string A(i.e., with characters 0 and 1) 
consisting of characters A1, A2, ..., AN. In a single operation, 
you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and 
flip the characters AL, AL+1, ..., AR. By flipping, 
we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final 
string number of 1s is maximized.

If you don't want to perform the operation, return an empty array.
 Else, return an array consisting of two elements denoting L and R. 
 If there are multiple solutions, return the lexicographically smallest 
 pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c
 or, if a == c and b < d.
Input 
A = "010"
[1, 1]
A = "010"

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"

We see that two pairs [1, 1] and [1, 3] 
give same number of 1s in final string. So, we return [1, 1].


'''
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        """using max sum subarray i.e kandaes algorithm
        store the indices for max sum
        Args:
            A (TYPE): binary string array
        """
        l,r = 0,0
        csum,maxsum = 0,0
        answer = [0,0]

        for i in range(len(A)):
            ch = A[i]

            if (ch == "1"):
                csum = csum - 1
            else:
                csum = csum + 1

            ## if current sum is greater than maximum sum store the indices
            if (csum > maxsum):
                maxsum = csum
                answer[0] = l+1 ## adding +1 as we are following 1 indexing
                answer[1] = r+1

            ## if current sum is negative then update left and right indices 
            ## i mean we need to move left and right indices and add +1 as we are following 1 indexing
            if csum < 0:
                csum = 0
                l = i + 1
                r = i + 1

            ## if current sum is greater than zero keep left index at same place and move right index
            else:
                r = r + 1 
        if maxsum == 0:
            return []
        return answer
sol = Solution()
A = "010"
print(sol.flip(A))

