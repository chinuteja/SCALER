'''
You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value 
in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater 
than equal to B.
If the target value is not found and least number greater than equal to
target is also not present, return the length of array 
(i.e. the position where target can be placed)

A = [1, 3, 5, 6]
B = 5
The target value is present at index 2. 


A = [1, 4, 9]
B = 3
The target value should be inserted at index 1.

'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def search(self,A,N,k):

        l = 0
        h = N - 1
        while(l <= h):
            mid = (l + h)//2

            if (A[mid] == k):
                return mid 
            elif (A[mid] < k):
                l = mid + 1
            else:
                h = mid - 1
        return l
    def searchInsert(self, A, B):
        index = self.search(A,len(A),B)
        return index


A = [1, 4, 9]
B = 3


A = [ 1, 3, 5, 6 ]
B = 7 

sol = Solution()
print(sol.searchInsert(A,B))