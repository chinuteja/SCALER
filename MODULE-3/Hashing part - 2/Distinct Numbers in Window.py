'''
You are given an array of N integers, A1, A2 ,..., AN and an integer B. 
Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array 
contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE: if B > N, return an empty array.


A = [1, 2, 1, 3, 4, 3]
B = 3

[2, 3, 3, 2]
A=[1, 2, 1, 3, 4, 3] and B = 3
 All windows of size B are
 [1, 2, 1]
 [2, 1, 3]
 [1, 3, 4]
 [3, 4, 3]
 So, we return an array [2, 3, 3, 2].
'''

class Solution:


    def dNums(self,A,B):

        k =B
        hm = {}
        output = []
        for i in range(k):
            if A[i] not in hm:
                hm[A[i]] = 1
            else:
                hm[A[i]] += 1
        output.append(len(hm))

        s = 1
        e = k

        while (e<len(A)):
            hm[A[s-1]]-= 1

            if hm[A[s-1]] == 0:
                del hm[A[s-1]]
            if A[e] not in hm:
                hm[A[e]] = 1
            else:
                hm[A[e]] += 1
            output.append(len(hm))
            e += 1
            s+= 1

        return output
sol = Solution()
A = [1, 2, 1, 3, 4, 3]
B = 3
A = [1, 1, 2, 2]
B = 1

print(sol.dNums(A,B))