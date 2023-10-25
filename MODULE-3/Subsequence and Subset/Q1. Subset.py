'''
A = [1, 2, 3]

output :
[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]

'''
# ans = []
# curr = []
# def solve(i, n, A):
#     global ans,curr
#     if i == n:
#         ans.append(sorted(curr.copy()))
#         return
#     # for every element we can either take it or skip it
#     solve(i + 1, n, A)
#     curr.append(A[i])
#     solve(i + 1, n, A)
#     curr.pop()
# class Solution:
#     # @param A : list of integers
#     # @return a list of list of integers
#     def subsets(self, A):
#         global ans,curr
#         ans = []
#         n = len(A)
#         solve(0, n, A)
#         return sorted(ans)




        

sol = Solution()
A = [1,2,3]
print(sol.subsets(A))
