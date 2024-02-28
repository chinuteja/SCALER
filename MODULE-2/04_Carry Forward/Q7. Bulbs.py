'''
A wire connects N light bulbs.

Each bulb has a switch associated with it; however, 
due to faulty wiring, a switch also changes the state of all 
the bulbs to the right of the current bulb.

Given an initial state of all bulbs, find the minimum number of 
switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.
Input :  A = [0, 1, 0, 1]

Output  4
press switch 0 : [1 0 1 0]
 press switch 1 : [1 1 0 1]
 press switch 2 : [1 1 1 0]
 press switch 3 : [1 1 1 1]
'''
class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):

		count = 0
		for i in range(len(A)):
			state = A[i]

			if i%2 == 0:
				A[i] = state
			else:
				A[i] = 1 - state
			if state == 0:
				count += 1
		return count