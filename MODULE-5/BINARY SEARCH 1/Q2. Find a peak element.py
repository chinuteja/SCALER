'''
Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its neighbors. 
or corner elements, we need to consider only one neighbor.
NOTE:

It is guaranteed that the array contains only a single peak element.
Users are expected to solve this in O(log(N)) time. 
The array may contain duplicate elements.


A = [5, 17, 100, 11]

Output 100


lazy approach find maximum element in an array
time complexity O(N)
'''
class Solution:
    

    def peak(self,A):
    	l = 0
    	h = len(A) - 1  

    	while (l <= h):
    		mid = (h + l )//2
    		
    		if A[mid] > A[mid + 1]:
    			r = mid 
    		else:
    			l = mid + l
    			
    	return A[l]  
    def solve(self, A):
        maximum = self.peak(A)
        return maximum


sol = Solution()
A = [5, 17, 100, 11]
A = [2,3]
print(sol.solve(A))
