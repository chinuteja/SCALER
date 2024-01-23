'''
Given an array of integers A of size N containing GCD of every possible 
pair of elements of another array.

Find and return the original numbers used to calculate the GCD array in 
any order. For example, if original numbers are {2, 8, 10} then the given
array will be {2, 2, 2, 2, 8, 2, 2, 2, 10}.

Input :  A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
Output :  [2, 8, 10]

Initially, array A = [2, 2, 2, 2, 8, 2, 2, 2, 10].
 2 is the gcd between 2 and 8, 2 and 10.
 8 and 10 are the gcds pair with itself.
 Therefore, [2, 8, 10] is the original array.

'''