class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count,ans = 0,0
        N = len(A)
        for i in range(N):
            if A[i] == "1":
                count += 1
        
        if count == N:
            return 1
        if count == 0:
            return 0

        for i in range(N):
            if(A[i] == "0"):
                left,right = 0,0

                j = i-1
                while(j >= 0):
                    if(A[j] == "1"):
                        left += 1
                    else:
                        break
                    j = j - 1
                
                r = i+1
                while(r<N):
                    if (A[r] == "1"):
                        right += 1
                    else:
                        break
                    r = r + 1
                k = left + right
                # print("k value is k",k)
                if k < count:
                    k += 1
                if k > ans:

                    ans = k
        return ans

obj = Solution()
print(obj.solve('1000010001111110100010101000111101111011001'))

####
