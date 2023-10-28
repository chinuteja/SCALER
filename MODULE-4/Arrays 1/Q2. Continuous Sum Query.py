'''
There are A beggars sitting in a row outside a temple.
 Each beggar initially has an empty pot. When the devotees come to the 
 temple, they donate some amount of coins to these beggars. 
 Each devotee gives a fixed amount of coin(according to their faith and 
 ability) to some K beggars sitting next to each other.

Given the amount P donated by each devotee to the beggars ranging from 
L to R index, where 1 <= L <= R <= A, find out the final amount of money in 
each beggar's pot at the end of the day, provided they don't fill their 
pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 
2D array B
Input:
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
Output:
10 55 45 25 25
First devotee donated 10 coins to beggars ranging from 1 to 2. 
Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
Second devotee donated 20 coins to beggars ranging from 2 to 3. 
Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
Third devotee donated 25 coins to beggars ranging from 2 to 5. 
Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]

'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve_brute_force(self, A, B):
        """
        Two loops so time complexity is O(N**2)
        Args:
            A (TYPE): number
            B (TYPE): array
        
        Returns:
            TYPE: Description
        """
        beggers_row = [0 for i in range(A)]
        for inner_list in B:
            left = inner_list[0]-1 ## as indices start from 0
            right = inner_list[1] - 1

            start_index = left
            end_index = right
            while (start_index <= end_index):
                beggers_row[start_index] += inner_list[2]
                start_index += 1
        return beggers_row

    def solve(self,A,B):
        """add value to start index and subtract same value to the end index
        at last do prefix sum
        Time complexity O(N)
        
        Args:
            A (TYPE): Description
            B (TYPE): Description
        
        Returns:
            TYPE: Description
        """
        beggers_row = [0 for i in range(A)]

        for inner_list in B:
            s = inner_list[0]-1
            e = inner_list[1] - 1
            val = inner_list[2]

            beggers_row[s] = beggers_row[s] + val
            if e < len(beggers_row)-1:
                beggers_row[e+1] = beggers_row[e+1] - val

        prefix_array = []
        prefix_array.append(beggers_row[0])

        for i in range(1,len(beggers_row)):
            prefix_array.append(beggers_row[i]+prefix_array[i-1])
        return prefix_array


sol = Solution()
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

A=5
B= [[1,1,5],[2,2,5],[3,4,5],[5,5,5]]
print(sol.solve_brute_force(A,B))
print(sol.solve(A,B))
