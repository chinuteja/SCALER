'''
Given an integer A representing the number of square blocks. 
The height of each square block is 1. 
The task is to create a staircase of max-height using these blocks.
The first stair would require only one block, 
and the second stair would require two blocks, and so on.
Find and return the maximum height of the staircase.

 A = 10

 The stairs formed will have height 1, 2, 3, 4.
Output 4 



'''
'''
We can solve this problem by realizing that the number of blocks required to
 build each step of the staircase forms an arithmetic series (1, 2, 3, ...). 
 To maximize the height of the staircase, we need to find the largest number (n) 
 in this series such that the sum of the series (1 + 2 + 3 + ... + n) does not 
 exceed the total number of blocks (A).

'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

    	i = 1
    	current_height = 0


    	while(i*(i+1)//2 <= A):

    		current_height = i
    		i += 1
    	return current_height

sol = Solution()
print(sol.solve(20))
