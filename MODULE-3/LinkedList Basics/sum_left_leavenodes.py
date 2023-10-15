class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, A):
        if A == None:
            return 0
        
        count = 0
        
        if A.left !=  None and A.left.left == None and A.left.right == None:
            count += A.left.val
        
        count += self.solve(A.left)
        count += self.solve(A.right)
        
        return count
