'''
Given an even number A ( greater than 2 ), 
return two prime numbers whose sum will be equal to the given number.

If there is more than one solution possible, 
return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is 
another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
eg 1048574

Output 3 1048571 
sum of  3 and 1048571 is 1048574

'''

def prime_numbers(N):
    primes = []
    for i in range(N+1):
        primes.append(True)
    primes[0] = False
    primes[1] = False
    for i in range(2,N+1,1):
        if (primes[i] == True):
            j = 2*i

            while (j<=N):
                primes[j] = False

                j += i
    output = {}
    for i in range(len(primes)):
        if primes[i] == True:
            output[i] = 0
    return output
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):

        output  = prime_numbers(A)

        answer = []
        for key in output:
            if (key in output) and (A-key in output):
                answer.append(key)
                answer.append(A-key)


        # if len(answer) == 2:
        #     return answer
        # A = answer[0]
        # B = answer[1]
        # final_answer = []
        # print(answer)
        # for i in range(2,len(answer)-1,2):
        #     C = answer[i]
        #     D = answer[i+1]

        #     if (((A < C) or (A == C)) and (B<D)):
        #         final_answer.append(A)
        #         final_answer.append(B)

        return answer[0:2]

sol = Solution()
#1048574
#184  181 3
print(sol.primesum(184))
