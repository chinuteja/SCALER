'''
You are given two positive numbers A and B . 
You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1

Input:
    A = 30
    B = 12
Output :
    5

 All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30). 
 The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
'''
import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def gcd(self,A,B):

        if A == 0:
            return B 
        if B == 0:
            return A 
        return self.gcd(B,A%B)

    def find_factors(self,A):

        factors_found = []

        for i in range(1,int(math.sqrt(A))+1):
            if A%i == 0:
                if (A//i == i):
                    factors_found.append(i)
                else:
                    factors_found.append(i)
                    factors_found.append(A//i)
        return factors_found

    def cpFact(self, A, B):

        ans = 0
        factors_found = self.find_factors(A)
        for factor in factors_found:
            gcd_caught = self.gcd(factor,B)
            if (gcd_caught == 1) and (ans < factor):
                ans = factor
                # print("answer ",ans)
        return ans

### Optimized solution

def gcd(A,B):
    if B==0:
        return A
    else:
        return gcd(B, A%B)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):

        while gcd(A,B)!= 1:
            A //= gcd(A,B)
       
        return A
sol = Solution()
a = 90
b = 47
print(sol.cpFact(a,b))
