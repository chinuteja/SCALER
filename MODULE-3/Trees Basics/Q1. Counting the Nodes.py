'''
Given the root of a tree A with each node having a 
certain value, find the count of nodes with more value than all its ancestors.

Ancestor means that every node that occurs before the current node 
in the path from root to the node.
Input
	4
   / \
  5   2
     / \
    3   6
Output : 3

The valid nodes are 4, 5 and 6.
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys 

class Solution:
    # @param A : root node of tree
    # @return an integer

    def no_nodes(self,node,max_value):
        if(node == None):
            return 0
        ans = 0
        if(node.val > max_value):
            max_value = node.val
            ans += 1
        ans += self.no_nodes(node.left,max_value)
        ans += self.no_nodes(node.right,max_value)
        return ans
    def solve(self, A):

        no_of_nodes = self.no_nodes(A,-999999999)
        return no_of_nodes 