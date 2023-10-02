class Solution:

    def extend(self,string,start,end):
        
        # print("string[start] == string[end]",string[start] == string[end])
        while((string[start] == string[end]) and (start>= 0) and (end<len(string))):
            
            start  = start-1
            end = end + 1

            if end == len(string):
                break

        return end-start-1,start+1,end-1
    def longestPalindrome(self,A):

        ans = 0
        for i in range(len(A)):
            # print(i)
            length,start_index,end_index= self.extend(A,i,i)
            # print("*"*10)
            if length > ans:
                ans = length
                require_start_index = start_index
                require_end_index = end_index
            

        for i in range(len(A)-1):
            length,start_index,end_index = self.extend(A,i,i+1)
            # print("length ",length,ans)
            if length > ans:
                ans = length
                require_start_index = start_index
                require_end_index = end_index
        # print("require_start_index",require_start_index,require_end_index)
        return A[require_start_index:require_end_index+1]

print("length of actual string ",len("abba"))
print(longestPalindrome("abba"))

# aaaabaaa



