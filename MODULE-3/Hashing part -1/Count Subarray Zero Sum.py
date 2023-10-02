# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pf = []
        pf.append(A[0])
        for i in range(1, len(A)):
            pf.append(pf[i-1] + A[i])
        freqmap = { 0 : 1 }
        # freqmap = {}
        count = 0
        print(pf)
        for num in pf:
            if num in freqmap:
                count += freqmap[num]
                freqmap[num] += 1
            else:
                freqmap[num] = 1
        return count % (10**9 + 7)


    def solve_new(self,A):
        '''
        with out prefix sum array
        '''
        hm = {0:1}
        sum_,count = 0,0
        for i in A:
            sum_ += i 
            if sum_ in hm:
                count += hm[sum_]
                hm[sum_] += 1
            else:
                hm[sum_] = 1
        return count
sol = Solution()
A = [1, -1, -2, 2]
print(sol.solve_new(A))