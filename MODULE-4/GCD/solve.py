'''

Scooby has 3 three integers A, B, and C.

Scooby calls a positive integer special if it is divisible by B and 
it is divisible by C. You need to tell the number of special integers less
 than or equal to A.
A = 12
 B = 3
 C = 2
Output : 2
 The two integers divisible by 2 and 3 and less than or equal to 12 are 6,12.

Hint
We can’t loop, so we can try for another approach, i.e., 
find the lcm(least common multiple) of B and C and find the number of
elements less than equal to A, which is divisible by lcm.
lcm(A,B)=(A*B)/(gcd(A,B))

'''


def bruteforce(A,B,C):
    count = 0
    for x in range(1,A+1):
        if (B%x == 0) and (C%x == 0) and (x<=A):
            count += 1
    return count

def gcd(A,B):
    if B==0:
        return A
    else:
        return gcd(B, A%B)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # print(gcd(B,C))
        lcm = (B*C)//gcd(B,C)
        print(lcm)

        return A//lcm

A = 6
B = 1
C = 4
# print(bruteforce(A,B,C))
sol = Solution()
print(sol.solve(A,B,C))