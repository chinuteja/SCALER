'''
You are given a string S, and 
you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).


Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC

'''
class Solution:

	def solve(self,A):
		count_vowel = 0
		A = A.lower()

		for i in A:
			if i in ["a","e","i","o","u"]:
				count_vowel += len(A)-i
		return count_vowel