'''
Say you have an array, A, for which the ith element is the price of a
 given stock on day i.
If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), 	
design an algorithm to find the maximum profit.

Return the maximum possible profit.


A = [1, 4, 5, 2, 4]

Output 4 
Buy the stock on day 0, and sell it on day 2.

'''
class Solution:
	# @param A : tuple of integers
	# @return an integer
	## Time complexity O(N**2)
	def maxProfit(self, A):

		max_profit = 0
		N = len(A)
		for i in range(N):
			buy = A[i]

			for j in range(i+1,N):
				sell = A[j]
				max_profit = max(max_profit,sell-buy)
		return max_profit



	def maxProfit_optimized(self,A):
		'''
		Hint you need to buy at low and sell at high
		traverse reverse
		'''
		if len(A) == 0:
			return 0    
		N = len(A)
		max_ = A[N-1]
		max_profit = 0
		i = N - 2
		
		while (i>=0):
			if max_ < A[i]:
				max_ = A[i]
			profit = max_-A[i]
			if max_profit < profit:
				max_profit = profit
			i = i - 1  
		return max_profit

A = [1,4,5,2,4]
A = [5,4,1,2,4]
sol = Solution()
print(sol.maxProfit(A))