'''
Given an array of integers A, 
find and return the count of divisors of each element of the array.

NOTE: The order of the resultant array should be the same as the input array.

Input :  A = [2, 3, 4, 5]
Output :  [2, 2, 3, 2]
The number of divisors of 2 : [1, 2], 3 : [1, 3], 4 : [1, 2, 4], 5 : [1, 5]
 So the count will be [2, 2, 3, 2].
'''


class Solution:
    
    def solve(self, A):


        ## Using Sieve (for smallest prime factor) and prime factorization (to get num of factors)
        n=max(A) + 1
        spf = [x for x in range(n)] #smallest prime factor

        for i in range(2,n):
            if spf[i] == i:
                for j in range(i*2, n, i):
                    spf[j] = i

        for i in range(len(A)):
            num = A[i]
            prime_factors={} ## using dict to avoid another loop i.e while (N%p == 0)
            while num > 1:
                pfactor = spf[num]
                num = num // pfactor
                if pfactor not in prime_factors:
                    prime_factors[pfactor] = 1
                else:
                    prime_factors[pfactor] += 1
               
            total_factors=1
            for x in prime_factors.values():
                total_factors *= x + 1
           
            A[i] = total_factors

        return A

sol = Solution()
A = [2, 3, 4, 5]
A = [8, 9, 10]
print(sol.solve(A))

