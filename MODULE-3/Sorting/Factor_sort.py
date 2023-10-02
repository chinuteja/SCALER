from functools import cmp_to_key
import math

class Solution:
    # @param A : list of integers
    # @return a list of integers

    def get_factors(self,num):


        k = int(math.sqrt(num))
        count = 0
        for i in range(1, k+1):
            if num % i == 0:

                if i == num//i:

                    count += 1
                else:
                    count += 2
        return count
    def solve(self, A):

        def comparator(a,b):
            factor_A = self.get_factors(a)
            factor_B = self.get_factors(b)

            if factor_A < factor_B:
                return -1
            if factor_A > factor_B:
                return 1
            if factor_A == factor_B:
                if a < b:
                    return -1
                if a > b:
                    return 1
                if a == b:
                    return 0
        sorted_array = sorted(A,key=cmp_to_key(comparator))
        return sorted_array

