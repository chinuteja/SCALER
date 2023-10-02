'''
A number can be broken into different consecutive sequence of digits. 
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different



'''

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        string = str(A)
        N = len(string)

        hm = {}
        for i in range(N):
            product = 1
            for j in range(i,N):
                product *= int(string[j])
                # print("product",product)

                if product in hm:
                    hm[product] += 1
                else:
                    hm[product] = 1
        for key in hm:
            value = hm[key]
            if value>1:
                return 0
        return 1
sol = Solution()
number = 236
print(sol.colorful(number))

