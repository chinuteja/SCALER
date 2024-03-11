'''
Given the array of strings A, you need to find the longest string S, 
which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S 
which is the 
prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc"
A = ["abab", "ab", "abcd"]
"ab"
'''

class Solution:
    
    def longestCommonPrefix(self,a):
        size = len(a)
    
        # if size is 0, return empty string
        if (size == 0):
            return ""
    
        if (size == 1):
            return a[0]
    
        # sort the array of strings
        a.sort()
        print(a)
        
        # find the minimum length from
        # first and last string
        end = min(len(a[0]), len(a[size - 1]))
        print("end ",end,a[0],a[size-1])
    
        # find the common prefix between
        # the first and last string
        i = 0
        while (i < end and
            a[0][i] == a[size - 1][i]):
            i += 1
    
        pre = a[0][0: i]
        return pre
sol = Solution()
A = ["abab", "ab", "abcd"]
# A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abcd","abcd","efgh"]
print(sol.longestCommonPrefix(A))

