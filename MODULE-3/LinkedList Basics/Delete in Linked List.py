'''
You are given the head of a linked list A and an integer B. 
Delete the B-th node from the linked list.

Note : Follow 0-based indexing for the node numbering.

Input A = 1 -> 2 -> 3
B = 1

Output 
1 -> 3
Input :
	A = 4 -> 3 -> 2 -> 1
	B = 0
Output :
	3 -> 2 -> 1

'''

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        if (B == 0):
            A = A.next
            # A.next = A.next.next
            return A
        temp = A
        for i in range(B-1):
            temp = temp.next
        kthnode = temp.next.next
        temp.next = kthnode
        return A
