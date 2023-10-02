class Solution:
    

    def binary_decimal(self,number):

        output = ""
        while (number != 0):
            remainder = number % 2
            number = number//2
            output = str(remainder)
        return output[::-1]


    def addBinary(self, A, B):
        sum_ = bin(int(A, 2) + int(B, 2))
        print("sum_",sum_[2:])
        return self.binary_decimal(sum_)

sol = Solution()
A = "100"
B = "11"

print(sol.addBinary(A,B))