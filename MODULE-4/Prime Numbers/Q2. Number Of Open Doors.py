# '''
# Given an integer A, which denotes the number of doors in a 
# row numbered 1 to A. All the doors are closed initially.

# A person moves to and fro, changing the states of the doors as 
# follows: the person opens a door that is already closed and closes a door 
# that is already opened.

# In the first go, he/she alters the states of doors numbered 1, 2, 3, … , A.
# In the second go, he/she alters the states of doors numbered 2, 4, 6 ….
# In the third go, he/she alters the states of doors numbered 3, 6, 9 …
# This continues till the A'th go in, which you alter the state of the door 
# numbered A.

# Find and return the number of open doors at the end of the procedure.

# A = 5
# Output  2
#  In the first go, he/she alters the states of doors numbered 1, 2, 3, 4, 5. 
#  Now, all doors are open.
#  In the second go, he/she closes the doors numbered 2, 4.
#  In the third go, he/she closes the door numbered 3.
#  In the fourth go, he/she open the door numbered 4.
#  In the fifth go, he/she closes the door numbered 5.
#  Doors opened at the end are 1 and 4.

# '''
import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

    	N = A+1

    	doors = []
    	for i in range(1,N+1):
    		doors.append(False)
    	# print("len fo doors ",len(doors))
    	for i in range(1,N):
    		doors[i] = True

    	i = 2

    	for i in range(1,N):

    		j = 2 * i

    		while(j<N):
    			# print(j)

    			if (doors[j] == True):
    				doors[j] = False

    			elif (doors[j] == False):
    				doors[j] = True
    			j = j + i
    	count = 0
    	for i in range(len(doors)):
    		if doors[i] == True:
    			# print(i)
    			count += 1
    	return count
## for a number which even no of factors the state is goanna be same
# for odd no factors state is going to change so only perfect squares will have odd factors

def optimized(A):

	count = 0
	for i in range(1,A+1):
		sqrt = math.sqrt(i)
		# print(math.sqrt(i))
		# print(i,"==>",int(math.sqrt(i))*int(math.sqrt(i)))
		# print()
		if int(math.sqrt(i))*int(math.sqrt(i)) == i:
			count += 1
	return count

print(optimized(100))

# sol = Solution()
# print("total no of doors ",sol.solve(6))